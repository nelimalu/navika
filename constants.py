FILEPATH = "c:\\dev\\python\\navika\\data.json"

# command response messages
STARTUP_MSG = "\n -- NAVIKA -- v1.0 -- LUKA JOVANOVIC -- "
LIST_MSG = "\n These are your current active habits:"
HELP_MSG = "\n Here is a list of all commands:"
NOT_FOUND_MSG = "That command doesn't exist. Try 'help'"

# error messages
ERROR_MSG = "[ERROR] "
SYNTAX_ERROR_MSG = " [SYNTAX ERROR] use the following format: "
VIEW_SYNTAX_MSG = "view <habit>"
LOG_SYNTAX_MSG = "log <habit> [amount] [date]"
CREATE_SYNTAX_MSG = "create <habit>"
DELETE_SYNTAX_MSG = "delete <habit>"
HELP_SYNTAX_MSG = "help"
LIST_SYNTAX_MSG = "list"
INFO_SYNTAX_MSG = "info <date>"
VIEWALL_SYNTAX_MSG = "viewall"
QUIT_SYNTAX_MSG = "quit"

SYNTAX_LIST = [
	VIEW_SYNTAX_MSG,
	LOG_SYNTAX_MSG,
	CREATE_SYNTAX_MSG,
	DELETE_SYNTAX_MSG,
	HELP_SYNTAX_MSG,
	LIST_SYNTAX_MSG,
	INFO_SYNTAX_MSG,
	VIEWALL_SYNTAX_MSG,
	QUIT_SYNTAX_MSG
]
