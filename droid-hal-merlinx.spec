# These and other macros are documented in dhd/droid-hal-device.inc
%define device merlinx
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 9

%define installable_zip 1

%define droid_target_aarch64 1

# Skip dynamic partitions in standard fstab generation
%define makefstab_skip_entries /system /vendor /product

%define straggler_files \
/bugreports\
/d\
/dsp\
/firmware\
/product\
/sdcard\
/system_ext\
%{nil}

%include rpm/dhd/droid-hal-device.inc
