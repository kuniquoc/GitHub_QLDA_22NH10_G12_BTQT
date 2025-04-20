# How To Improve A Standard Control

Frappe has a couple of elegant and useful widgets, but sometimes we need to edit them to add small improvements. This article describes how to add new resources to the standard widgets.

## Example Goal

Add many alternative translations in numerous records and in a lot of DocTypes. To achieve this, we need to improve the control or widget.

## Implementation

We define a word to put in the `options` of the `DocFields` that we need to include the feature. This word will be `Translatable`.

### Code Example

```javascript
frappe.ui.form.ControlData = frappe.ui.form.ControlData.$extend({
    make_input: function() {
        var options = this.df.options;
        if (!options || options !== "Translatable") {
            this._super();
            return;
        }
        var me = this;
        $('<div>').prependTo(this.input_area);
        this.$input_area = $(this.input_area);
        this.$input = this.$input_area.find('input');
        this.$btn = this.$input_area.find('.dialog-btn');
        this.set_input_attributes();
    },
    setup_button: function() {
        var me = this;
        this.$btn.on("click", function() {
            var value = me.get_value();
            if (value && me.df.options === "Translatable") {
                me.open_dialog();
            }
        });
    },
    open_dialog: function() {
        new frappe.ui.form.TranslationSelector({
            doc: this.frm.doc,
            df: this.df,
            text: this.value
        });
    }
});
```