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
# Android 16 init.rc starts odsign in post-fs-data and waits for
# odsign.key.done; odsign cannot run on Sailfish OS (needs the statsd APEX and
# is only for ART), so init would stall before starting the HALs.
%define custom_install_cmds \
sed -i -e '/^ *start odsign$/s/start/# Removed for Sailfish OS: start/' -e '/^ *wait_for_prop odsign.key.done 1$/s/wait_for_prop/# Removed for Sailfish OS: wait_for_prop/' $RPM_BUILD_ROOT%{_libexecdir}/droid-hybris/system/etc/init/hw/init.rc \
test $(grep -cE "^ *# Removed for Sailfish OS: (start odsign|wait_for_prop odsign.key.done 1)$" $RPM_BUILD_ROOT%{_libexecdir}/droid-hybris/system/etc/init/hw/init.rc) -eq 2 || exit 1 \
%{nil}
%include rpm/dhd/droid-hal-device.inc
