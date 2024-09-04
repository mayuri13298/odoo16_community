/** @odoo-module **/

import { registry } from "@web/core/registry";
import { CharField } from "@web/views/fields/char/char_field";
import Widget from 'web.Widget';

const { useState } = owl;
export class PasswordWidget extends CharField { // Changed to extend from CharField
    setup() {
        super.setup();
    }

    onIconClick() {
        var node = $('.password').attr('type')
        if (node == 'password') {
            $('.password').prop('type', 'text');
            $('i').toggleClass("fa-eye");
            $('i').removeClass("fa-eye-slash");
        } else {
            $('.password').prop('type', 'password');
            $('i').toggleClass("fa-eye-slash");
            $('i').removeClass("fa-eye");
        }
    }
}

PasswordWidget.template = "password_widget.FieldPassword";

registry.category("fields").add("password", PasswordWidget);