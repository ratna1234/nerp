$(document).ready(function () {
    vm = new ReceiptVM(ko_data);
    ko.applyBindings(vm);
    $('.change-on-ready').trigger('change');
});

function BudgetVM(data) {
    var self = this;
    for (var k in data) {
        self[k] = ko.observable(data[k]);
    }

}

function ReceiptVM(data) {

    var self = this;

    self.parse_error = function(data){
        console.log('hey');
        console.log(data);
        return 'hey';
    }

    $.ajax({
        url: '/budget_heads.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.budget_heads = ko.observableArray(ko.utils.arrayMap(data, function (item) {
                return new BudgetVM(item);
            }));
//            self.budget_heads = ko.observableArray(data);
        }
    });

    $.ajax({
        url: '/tax_schemes.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.tax_schemes = ko.observableArray(data);
        }
    });

    $.ajax({
        url: '/accounts.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.accounts = ko.observableArray(data);
        }
    });

    $.ajax({
        url: '/donors.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.donors = ko.observableArray(data);
        }
    });

    $.ajax({
        url: '/activities.json',
        dataType: 'json',
        async: false,
        success: function (data) {
            self.activities = ko.observableArray(data);
        }
    });

    self.sort = function () {
        console.log('hey');

    }

//    self.errors = new ko.observableDictionary({});

//    self.errors = ko.observable({});

    self.errors = new HashTable();

    self.msg = ko.observable('');
    self.status = ko.observable('standby');

    self.item_changed = function (row) {
        var selected_item = $.grep(self.items(), function (i) {
            return i.id == row.item_id();
        })[0];
        if (!selected_item) return;
        row.specification(selected_item.description);
        row.unit(selected_item.unit);
        row.inventory_account_id(selected_item.account_no);
    }

    self.table_view = new TableViewModel({rows: data.rows, argument: self}, ReceiptRowVM);

    for (var k in data)
        self[k] = ko.observable(data[k]);

    self.save = function (item, event) {
        $.ajax({
            type: "POST",
            url: '/account/receipt/save/',
            data: ko.toJSON(self),
            success: function (msg) {
                if (typeof (msg.error_message) != 'undefined') {
                    alert.error(msg.error_message);
                }
                else {
                    alert.success('Saved!');
                    if (msg.id)
                        self.id(msg.id);
                    $("#tbody > tr").each(function (i) {
                        $($("#tbody > tr")[i]).addClass('invalid-row');
                    });
                    for (var i in msg.rows) {
                        self.table_view.rows()[i].id = msg.rows[i];
                        $($("#tbody > tr")[i]).removeClass('invalid-row');
                    }
                }
            }
//            error: function(XMLHttpRequest, textStatus, errorThrown) {
//                $('#message').html(XMLHttpRequest.responseText.message);
//            }
        });
    }


}

function ReceiptRowVM(row, root) {

    var self = this;
    //default values

    self.budget_head = ko.observable([]);
    self.budget_head_id = ko.observable();
    self.account = ko.observable([]);
    self.account_id = ko.observable();
    self.tax_scheme = ko.observable([]);
    self.tax_scheme_id = ko.observable();
    self.activity = ko.observable([]);
    self.activity_id = ko.observable();

    self.invoice_no = ko.observable();
    self.remarks = ko.observable();

    self.nepal_government = ko.observable(11);
    self.foreign_cash_grant = ko.observable();
    self.foreign_compensating_grant = ko.observable();
    self.foreign_cash_loan = ko.observable();
    self.foreign_compensating_loan = ko.observable();
    self.foreign_substantial_aid = ko.observable();

    for (var k in row) {
        if (row[k] != null)
            self[k] = ko.observable(row[k]);
    }

    self.nepal_government.subscribe(function () {
        self.check_due('nepal_government');
    });

    self.foreign_cash_grant.subscribe(function () {
        self.check_due('foreign_cash_grant');
    });

    self.foreign_compensating_grant.subscribe(function () {
        self.check_due('foreign_compensating_grant');
    });

    self.foreign_cash_loan.subscribe(function () {
        self.check_due('foreign_cash_loan');
    });

    self.foreign_compensating_loan.subscribe(function () {
        self.check_due('foreign_compensating_loan');
    });

    self.foreign_substantial_aid.subscribe(function () {
        self.check_due('foreign_substantial_aid');
    });

    self.check_due = function (source) {
        var due = self.budget_head().current_balance()[source + '_due'];
        var sum = 0;
        for (var k in root.table_view.rows()) {
            var row = root.table_view.rows()[k];
            if (typeof row[source]() != 'undefined')
                sum += parseFloat(row[source]());
        }

        if (sum > due) {
            root.errors.push_lazy({budget: self.budget_head(), source: source });
        } else {
            root.errors.remove({budget: self.budget_head(), source: source })
        }
    }

    self.advanced = ko.observable();
    self.advanced_settlement = ko.observable();
    self.cash_returned = ko.observable();

    self.vattable = ko.observable(false);


    self.amount = function () {
        return r2z(self.nepal_government()) + r2z(self.foreign_cash_grant()) + r2z(self.foreign_compensating_grant()) + r2z(self.foreign_cash_loan()) + r2z(self.foreign_compensating_loan()) + r2z(self.foreign_substantial_aid());
    }

    self.vat_amount = function () {
        if (self.vattable()) {
            return self.amount() * 0.13;
        }
        return '';
    }

    self.tax_amount = function () {
        return r2z(parseFloat(self.tax_scheme().percent) * self.amount() / 100);
    }

    self.payable_amount = function () {
        return r2z(self.amount() + self.tax_amount());
    }


    self.amount_focused = function (row, e) {
        $(e.currentTarget).click();
    }

    self.vattable_focused = function (row, e) {
        Foundation.libs.dropdown.close($('#drop' + $(e.currentTarget).data('index')));
    }

    self.has_balance = function (source) {
        if (!Object.size(self.budget_head())) {
            return false;
        }
        if (self.budget_head().current_balance()) {
            var balance = parseFloat(self.budget_head().current_balance()[source + '_due']);
            if (balance > 0)
                return true;
        }
        return false;
    }

    self.has_foreign = function () {
        return self.has_balance('foreign_cash_grant') || self.has_balance('foreign_compensation_grant') || self.has_balance('foreign_cash_loan') || self.has_balance('foreign_compensating_loan') || self.has_balance('foreign_substantial_aid')
    }


}