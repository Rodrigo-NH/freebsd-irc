###
# Copyright (c) 2019, Rodrigo
# All rights reserved.
#
#
###

from supybot import conf, registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Loglogger')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Loglogger', True)


Loglogger = conf.registerPlugin('Loglogger')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Loglogger, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerGlobalValue(Loglogger, 'Channel',
    registry.String('', """Sets the channel where LogLogger should inform login events"""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
