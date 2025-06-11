from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_drag_and_drop(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    # Esperamos a que los elementos estén presentes
    column_a = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "column-a"))
    )
    column_b = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "column-b"))
    )

    # JavaScript para simular drag and drop
    drag_and_drop_script = """
    function simulateDragDrop(sourceNode, destinationNode) {
        var EVENT_TYPES = {
            DRAG_END: 'dragend',
            DRAG_START: 'dragstart',
            DROP: 'drop'
        }

        function createCustomEvent(type) {
            var event = new CustomEvent("CustomEvent")
            event.initCustomEvent(type, true, true, null)
            event.dataTransfer = {
                data: {},
                setData: function(type, val) {
                    this.data[type] = val
                },
                getData: function(type) {
                    return this.data[type]
                }
            }
            return event
        }

        function dispatchEvent(node, type, event) {
            if (node.dispatchEvent) {
                return node.dispatchEvent(event)
            }
            if (node.fireEvent) {
                return node.fireEvent("on" + type, event)
            }
        }

        var dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START)
        dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent)

        var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
        dropEvent.dataTransfer = dragStartEvent.dataTransfer
        dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

        var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
        dragEndEvent.dataTransfer = dragStartEvent.dataTransfer
        dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
    }

    var source = arguments[0]
    var target = arguments[1]
    simulateDragDrop(source, target)
    """

    # Ejecutar el JS para mover A hacia B
    driver.execute_script(drag_and_drop_script, column_a, column_b)

    # Verificamos si el texto se ha intercambiado correctamente
    column_a_header = column_a.find_element(By.TAG_NAME, "header").text
    column_b_header = column_b.find_element(By.TAG_NAME, "header").text

    assert column_a_header == "B", "No se hizo el intercambio correctamente en A"
    assert column_b_header == "A", "No se hizo el intercambio correctamente en B"
