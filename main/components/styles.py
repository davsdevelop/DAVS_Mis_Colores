
# -----------------------------------------------------------------------------
# Layout general
# -----------------------------------------------------------------------------
# Cambiamos a un gris oscuro profundo/pizarra para el fondo de la pantalla
PAGE = "flex flex-col min-h-screen w-full bg-[#0F172A]" 
CONTENT_WRAPPER = "max-w-[1400px] w-full mx-auto px-6 py-6"
GRID_3_COLS = "grid grid-cols-3 gap-5 w-full"
COL_SPAN_2 = "col-span-2"
COL_SPAN_1 = "col-span-1"

# -----------------------------------------------------------------------------
# Tarjetas contenedoras
# -----------------------------------------------------------------------------
CARD = "p-6 bg-white rounded-3xl shadow-[0_2px_20px_rgba(0,0,0,0.06)] w-full"
CARD_SCROLLABLE = (
    "p-6 bg-white rounded-3xl shadow-[0_2px_20px_rgba(0,0,0,0.06)] "
    "w-full h-fit max-h-[calc(100vh-120px)] overflow-y-auto"
)

# -----------------------------------------------------------------------------
# Navbar
# -----------------------------------------------------------------------------
# Ajustamos el borde inferior para que sea sutil sobre el fondo negro
NAVBAR_WRAPPER = "sticky top-0 z-50 border-b border-white/[0.08]"
NAVBAR_INNER = "flex items-center gap-4 max-w-[1400px] mx-auto w-full px-6 py-4"
NAVBAR_LOGO = "flex items-center gap-2"
NAVBAR_LOGO_ICON = "text-red-500"
# Cambiamos text-black a text-white para que resalte sobre el fondo negro del navbar
NAVBAR_LOGO_TEXT = "text-lg text-white font-bold tracking-tight" 
NAVBAR_ACTIONS = "flex items-center gap-2"

# -----------------------------------------------------------------------------
# Botones
# -----------------------------------------------------------------------------
BTN_BASE = "flex items-center gap-2 text-sm font-medium transition-colors cursor-pointer border-none"
BTN_GHOST = BTN_BASE + " px-4 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-700"
BTN_GHOST_RED = BTN_BASE + " px-4 py-2 rounded-lg bg-red-50 hover:bg-red-100 text-red-700" # <-- Nueva variable rojiza
BTN_PRIMARY = BTN_BASE + " px-4 py-2 rounded-lg bg-red-600 hover:bg-red-700 text-white" # <-- Cambiado a rojo
BTN_SUCCESS = BTN_BASE + " px-4 py-2 rounded-lg bg-emerald-100 hover:bg-emerald-200 text-emerald-700"
BTN_ICON = (
    "w-7 h-7 flex items-center justify-center rounded-md "
    "hover:bg-gray-100 text-gray-500 cursor-pointer transition-colors"
)
BTN_ICON_DANGER = (
    "w-7 h-7 flex items-center justify-center rounded-md "
    "hover:bg-red-50 text-red-400 cursor-pointer transition-colors"
)

# -----------------------------------------------------------------------------
# Color card
# -----------------------------------------------------------------------------
COLOR_CARD = (
    "flex flex-col justify-center items-center rounded-full aspect-square w-full "
    "overflow-hidden shadow-[0_4px_20px_rgba(0,0,0,0.15)] transition-all duration-200 "
    "hover:-translate-y-1 hover:shadow-[0_12px_40px_rgba(0,0,0,0.25)]"
)
# Cambiamos a flex-col y justify-center para que el texto y el botón queden al centro del círculo
COLOR_CARD_FOOTER = "flex flex-col items-center justify-center gap-2 w-full"
COLOR_CARD_HEX_CHIP = "bg-black/25 rounded-full px-3 py-1"
COLOR_CARD_HEX_TEXT = "text-xs font-bold text-white"
COLOR_CARD_ACTIONS = "flex items-center gap-1"
COLOR_CARD_BTN = "text-white cursor-pointer hover:opacity-70 transition-opacity"
COLOR_CARD_WRAPPER = "flex flex-col items-center gap-2 w-full"
COLOR_CARD_REMOVE_BTN = (
    "w-full flex items-center justify-center gap-1 py-1 rounded-xl "
    "text-xs font-medium text-red-400 hover:text-red-600 hover:bg-red-50 "
    "transition-colors cursor-pointer border-none bg-transparent"
)

# -----------------------------------------------------------------------------
# Palette editor
# -----------------------------------------------------------------------------
EDITOR_HEADER = "flex items-center mb-6"
EDITOR_TITLE = "text-2xl font-bold tracking-tight text-gray-900"
EDITOR_SUBTITLE = "text-sm text-gray-400 mt-0.5"


# -----------------------------------------------------------------------------
# Saved palettes
# -----------------------------------------------------------------------------
PALETTES_TITLE = "text-2xl font-bold tracking-tight text-gray-900"
PALETTES_COUNT = "text-sm text-gray-400 mt-0.5 mb-5"
PALETTES_LIST = "flex flex-col gap-2 w-full"

PALETTE_ROW = (
    "p-3 rounded-2xl bg-black/[0.02] border border-black/[0.06] "
    "hover:bg-black/[0.05] transition-colors w-full"
)
PALETTE_ROW_PREVIEW = "w-full h-14 rounded-xl"
PALETTE_ROW_INFO = "flex items-center mt-2"
PALETTE_ROW_NAME = "text-sm font-medium text-gray-800 truncate max-w-[130px]"
PALETTE_ROW_DATE = "text-xs text-gray-400"
PALETTE_ROW_BTNS = "flex items-center gap-0.5"

EMPTY_STATE = "flex flex-col items-center justify-center py-12 w-full"
EMPTY_STATE_ICON = "text-gray-300"
EMPTY_STATE_TEXT = "text-sm text-gray-400 mt-2"
EMPTY_STATE_SUBTEXT = "text-xs text-gray-300"

# -----------------------------------------------------------------------------
# Modales (dialogs)
# -----------------------------------------------------------------------------
DIALOG_CONTENT = "max-w-sm w-full rounded-2xl bg-white shadow-xl p-0 overflow-hidden"
DIALOG_INNER = "p-6"
DIALOG_TITLE = "text-lg font-bold text-gray-900"
DIALOG_DESC = "text-sm text-gray-500 mt-1"
DIALOG_INPUT = (
    "w-full mt-4 px-3 py-2 rounded-lg border border-gray-200 text-sm "
    "focus:outline-none focus:ring-2 focus:ring-blue-400"
)
DIALOG_ACTIONS = "flex justify-end gap-3 mt-4"
