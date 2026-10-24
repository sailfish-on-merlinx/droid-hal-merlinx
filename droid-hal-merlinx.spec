# These and other macros are documented in dhd/droid-hal-device.inc
%define device merlinx
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 9
%define installable_zip 1
%define droid_target_aarch64 1
# Logical partitions in super: mapped by dmsetup.service and mounted by
# custom units in droid-config (HADK-hot: dynamic partitions)
%define makefstab_skip_entries /system /system_ext /vendor /product
%define straggler_files \
/adb_keys\
/bugreports\
/d\
/product\
/sdcard\
/system_ext\
%{nil}
%include rpm/dhd/droid-hal-device.inc
