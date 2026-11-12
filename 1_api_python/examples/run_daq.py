from api import DeviceAPI
from logging import basicConfig, DEBUG, INFO


if __name__ == "__main__":
    basicConfig(level=INFO)

    DeviceAPI().do_reset()
    dut = DeviceAPI()
    dut.define_channel_layout(
        channel_layout=[[1, 2], [3, 4], [5, 6], [7, 8]],
        channel_names=["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"],
        channel_units=["LSB", "LSB", "LSB", "LSB", "LSB", "LSB", "LSB", "LSB"]
    )
    dut.start_daq(
        sampling_rate=1000.0,
        do_plot=True,
        do_record=True,
        do_process=False,
        window_sec=10.0,
    )
    dut.stop_daq()
