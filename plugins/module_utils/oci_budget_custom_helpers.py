# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


# Having message as a top level parameter causes issues in ansible when journal
# is enabled. Check https://github.com/ansible/ansible/issues/47132 for more
# details. To get around this problem, the name of the parameter is changed to
# msg. But since these are existing modules and it does work when journal is not
# enabled, adding message as an alias so that it is not a breaking change. The
# below customisations are needed since the rename is in the module but we
# still have to pass the values with original names to SDK/API.
class BudgetAlertRuleHelperCustom:
    def get_create_model(self):
        create_model = super(BudgetAlertRuleHelperCustom, self).get_create_model()
        if self.module.params.get("msg"):
            setattr(create_model, "message", self.module.params["msg"])
        return create_model

    def get_update_model(self):
        update_model = super(BudgetAlertRuleHelperCustom, self).get_update_model()
        if self.module.params.get("msg"):
            setattr(update_model, "message", self.module.params["msg"])
        return update_model
