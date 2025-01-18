import esphome.codegen as cg
from esphome.components import sensor, uart

# from esphome.const import CONF_POWER

DEPENDENCIES = ["uart"]

viessmannconnect_ns = cg.esphome_ns.namespace("viessmann_connect")
ViessmannConnectComponent = viessmannconnect_ns.class_(
    "ViessmannConnectComponent", sensor.Sensor, cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = sensor.sensor_schema(ViessmannConnectComponent).extend(
    uart.UART_DEVICE_SCHEMA
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "viessmannconnect",
    baud_rate=4800,
    require_tx=False,
    require_rx=True,
    data_bits=8,
    parity=None,
    stop_bits=1,
)


async def to_code(config):
    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
