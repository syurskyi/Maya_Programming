import maya.cmds as cmds
import maya.mel as mel


class RetimingUtils(object):

    @classmethod
    def retime_keys(cls, retime_value, incremental, move_to_next):
        range_start_time, range_end_time = cls.get_selected_range()
        start_keyframe_time = cls.get_start_keyframe_time(range_start_time)
        last_keyframe_time = cls.get_last_keyframe_time()
        current_time = start_keyframe_time

        new_keyframe_times = [start_keyframe_time]

        while current_time != last_keyframe_time:
            next_keyframe_time = cls.find_keyframe("next", current_time)

            if incremental:
                time_diff = next_keyframe_time - current_time
                if current_time < range_end_time:
                    time_diff += retime_value
                    if time_diff < 1:
                        time_diff = 1
            else:
                if current_time < range_end_time:
                    time_diff = retime_value
                else:
                    time_diff = next_keyframe_time - current_time

            new_keyframe_times.append(new_keyframe_times[-1] + time_diff)
            current_time = next_keyframe_time

        if len(new_keyframe_times) > 1:
            cls.retime_keys_recursive(start_keyframe_time, 0, new_keyframe_times)


    @classmethod
    def retime_keys_recursive(cls, current_time, index, new_keyframe_times):
        if index >= len(new_keyframe_times):
            return

        updated_keyframe_time = new_keyframe_times[index]

        next_keyframe_time = cls.find_keyframe("next", current_time)

        if updated_keyframe_time < next_keyframe_time:
            cls.change_keyframe_time(current_time, updated_keyframe_time)
            cls.retime_keys_recursive(next_keyframe_time, index + 1, new_keyframe_times)
        else:
            cls.retime_keys_recursive(next_keyframe_time, index + 1, new_keyframe_times)
            cls.change_keyframe_time(current_time, updated_keyframe_time)

    @classmethod
    def set_current_time(cls, time):
        cmds.currentTime(time)

    @classmethod
    def get_selected_range(cls):
        playback_slider = mel.eval("$tempVar = $gPlayBackSlider")
        selected_range = cmds.timeControl(playback_slider, q=True, rangeArray=True)

        return selected_range

    @classmethod
    def find_keyframe(cls, which, time=None):
        kwargs = {"which": which}
        if which in ["next", "previous"]:
            kwargs["time"] = (time, time)

        return cmds.findKeyframe(**kwargs)

    @classmethod
    def change_keyframe_time(cls, current_time, new_time):
        cmds.keyframe(e=True, time=(current_time, current_time), timeChange=new_time)

    @classmethod
    def get_start_keyframe_time(cls, range_start_time):
        start_times = cmds.keyframe(q=True, time=(range_start_time, range_start_time))
        if start_times:
            return start_times[0]

        start_time = cls.find_keyframe("previous", range_start_time)
        return start_time

    @classmethod
    def get_last_keyframe_time(cls):
        return cls.find_keyframe("last")


if __name__ == "__main__":

    # print(RetimingUtils.get_last_keyframe_time())
    RetimingUtils.retime_keys(2, False, False)
