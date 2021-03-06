#
# PySNMP MIB module BCSSIMULCRYPTSCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BCSSIMULCRYPTSCS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
bcs, = mibBuilder.importSymbols("BCS-IDENT-MIB", "bcs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Counter32, TimeTicks, IpAddress, Counter64, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Unsigned32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter32", "TimeTicks", "IpAddress", "Counter64", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsSimulcryptScs = ModuleIdentity((1, 3, 6, 1, 4, 1, 1166, 7, 7))
bcsSimulcryptScs.setRevisions(('2009-10-01 00:00', '2009-05-10 00:00', '2006-02-09 00:00', '2004-08-09 00:00', '2004-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcsSimulcryptScs.setRevisionsDescriptions(('Version 1.4; October 1, 2009 By RXF637 - Changed comments/range for bcsSimScsEcmChannelTestPeriodicity', "Version 1.3; May 10, 2009 By RXF637 - Added bcsSimScsEcmChannelTestPeriodicity - Added bcsSimScsEcmNetworkDelay - Added bcsSimScsEcmReplyTimeout - Added bcsSimScsEcmgRedundancyConfigTable - Added bcsSimScsEcmgRedundancyConfigApplyTable First Three are the New Scalar parameters for ECMG's and Last 2 are the New ECMG Redundancy Tables. ", 'Version 1.2; February 9, 2006 - Updated Contact Information.', 'Version 1.2: May 9, 2008 - Added new enumeration, serviceId, to bcsSimScsAccessCriteriaSource. August 09, 2004 - Changed description of bcsSimScsAccessCriteriaSource. July 27, 2004 - Changed enumerations for bcsSimScsAccessCriteriaSource.', 'Version 1.0: June 24, 2003 - Initial Revision.',))
if mibBuilder.loadTexts: bcsSimulcryptScs.setLastUpdated('200905100000Z')
if mibBuilder.loadTexts: bcsSimulcryptScs.setOrganization('Motorola Connected Home Solutions')
if mibBuilder.loadTexts: bcsSimulcryptScs.setContactInfo('Motorola Technical Response Center Inside USA 1-888-944-HELP (1-888-944-4357) Outside USA 1-215-323-0044 TRC Hours: Monday through Friday 8am - 7pm Eastern Standard Time Saturdays 10am - 5pm Eastern Standard Time')
if mibBuilder.loadTexts: bcsSimulcryptScs.setDescription('The Simulcrypt SCS MIB module for Motorola BCS products.')
class ApplyDataToDeviceTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("applyNotInProgress", 1), ("apply", 2), ("applyNotInProgressValidData", 3), ("applyNotInProgressInvalidData", 4))

class ManualSwitchBackTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manualSwitchBackNotInProgress", 1), ("manualSwitchBack", 2))

bcsSimScsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1))
bcsSimScsConfigGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1))
bcsSimScsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2))
bcsSimScsStatusGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1))
class EnableDisableTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

bcsSimScsNetworkId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsNetworkId.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsNetworkId.setDescription('This parameter specifies the network ID used for this Simulcrypt system. The network ID is a Simulcrypt system parameter, please see Simulcrypt system specifications for a more detailed explanation. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsMaxNetworkDelay = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsMaxNetworkDelay.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsMaxNetworkDelay.setDescription('Worst case propagation delay, in milliseconds, introduced by network topology. Will be factored into negotiations of the actual Simulcrypt crypto-period. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsNominalCryptoPeriod = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsNominalCryptoPeriod.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsNominalCryptoPeriod.setDescription('This value specifies the nominal crypto-period in seconds. This value is used as a target for this device during crypto- period negotiations. The actual negotiated crypto-period may be equal to or greater than this value. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsAccessCriteriaSource = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dtviaFixedAc", 1), ("noAc", 2), ("serviceId", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsAccessCriteriaSource.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsAccessCriteriaSource.setDescription('This value specifies which vendor will provide the access criteria information. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsEcmgTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgTimeout.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgTimeout.setDescription('This parameter specifies how long the SCS should wait for a response from the ECMG. This value is specified in seconds. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsEcmIdInitial = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmIdInitial.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmIdInitial.setDescription('Each ECM ID and Super CAS ID combination in the Simulcrypt system must be globally unique. To simplify configuration, each SCS is given a starting ECM ID to assign to the first ECM stream it creates. The number is incremented as new ECM streams are created. Each SCS must be configured with a different value. The initial values should be spaced sufficiently to prevent overlapping. Recommended spacing is 128. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsEcmChannelTestPeriodicity = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmChannelTestPeriodicity.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmChannelTestPeriodicity.setDescription("Periodicity for the channel test procedure.Default set to 20sec. @Range(min=1, max=3600) @Config(config=yes, reboot=no) @Save(semSaveConfig, value=2, default=yes) @File(config.ini, type='ini') ")
bcsSimScsEcmNetworkDelay = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmNetworkDelay.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmNetworkDelay.setDescription("The network delay value to account for delays while waiting on an ECM response.Default set to 500msec. @Range(min=0, max=30000) @Config(config=yes, reboot=no) @Save(semSaveConfig, value=2, default=yes) @File(config.ini, type='ini') ")
bcsSimScsEcmReplyTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmReplyTimeout.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmReplyTimeout.setDescription("Time to wait before timing out while waiting on a response to a channel/stream management message (i.e.: channel_setup, channel_test, stream_setup).Default set to 4000 msec. @Range(min=100, max=60000) @Config(config=yes, reboot=no) @Save(semSaveConfig, value=2, default=yes) @File(config.ini, type='ini') ")
bcsSimScsEcmgConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2), )
if mibBuilder.loadTexts: bcsSimScsEcmgConnectionTable.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectionTable.setDescription('This table persists the Simulcrypt SCS to ECMG connections or channels. The device will send Simulcrypt control words to a maximum of bcsSimScsMaxEcmg.')
bcsSimScsEcmgConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgConnectIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectionEntry.setDescription('A single entry in the bcsSimScsEcmgConnectionTable table.')
bcsSimScsEcmgConnectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsSimScsEcmgConnectIndex.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectIndex.setDescription('The Simulcrypt ECMG Connection table index.')
bcsSimScsEcmgConnectEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 2), EnableDisableTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectEnabled.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectEnabled.setDescription('Each row in the bcsSimScsEcmgConnectionTable represents a potential SCS<=>ECMG connection that will be attempted during simulcrypt SCS initialization. This setting controls whether or not the attempt is made. This setting has two legal settings: disabled (1) <= The connection will be attempted. enabled (2) <= The connection will not be attempted. Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsEcmgConnectSuperCasId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectSuperCasId.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectSuperCasId.setDescription("The Super CAS ID of the ECMG that will be connected to by the Simulcrypt SCS. The Super CAS ID is the 32 bit concatenation of the CAS ID and the Sub CAS ID. The CAS ID identifies the Conditional Access provider. It supplies the upper 16 bits of the SuperCAS ID. The Sub CAS ID identifies instances of a provider's ECMGs on the Simulcrypt network. It supplies the lower 16 bits of the Super CAS ID. Each ECM ID and SuperCAS ID combination in the Simulcrypt system must be globally unique. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.")
bcsSimScsEcmgConnectIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectIpAddr.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectIpAddr.setDescription('The IP address that the ECMG is listening on. Used to open a socket between the SCS and the ECMG. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsEcmgConnectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectPort.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgConnectPort.setDescription('The remote port that the ECMG is listening on. Used to open a socket between the SCS and the ECMG. SEM Note: Once written, a save must be performed via the semSaveConfig parameter and the SEM must be rebooted for the change to take effect.')
bcsSimScsEcmgRedundancyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3), )
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigTable.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigTable.setDescription("This table configures parameters associated with the ECMG redudancy feature. @Commit(param=bcsSimScsEcmgRedundancyConfigApplyChange, value=2) @Save(semSaveConfig, value=2) @File(config.ini, type='ini') ")
bcsSimScsEcmgRedundancyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgRedundancyConfigIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigEntry.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigEntry.setDescription('A single entry in bcsSimScsEcmgRedundancyConfigTable.')
bcsSimScsEcmgRedundancyConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigIndex.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigIndex.setDescription('Index into the table.')
bcsSimScsEcmgRedundancyConfigAutoSwitchBack = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 2), EnableDisableTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigAutoSwitchBack.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigAutoSwitchBack.setDescription('If enabled (2), programs (which were taken away earlier from this ECMG upon its failure) will be automatically switched back to this ECMG after its recovery. If disabled (1), such an automatic switching will not happen. Detailed semantics are captured in requirements.Default value is enabled.')
bcsSimScsEcmgRedundancyConfigManualSwitchBack = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 3), ManualSwitchBackTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigManualSwitchBack.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigManualSwitchBack.setDescription('When autoswitchback is enabled manual switch back is notActive.When manual switch back Button get pressed Manual switch back state get changed from manualSwitchBackNotInProgress(1) to (2)manualSwitchBack.Then the programs (which were taken away earlier from this ECMG upon its failure)will be switched back to it. Once the switchback progress get finished ,manual switch back state changed to (1) manualSwitchBackNotInProgress.')
bcsSimScsEcmgRedundancyConfigMaxStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigMaxStreams.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigMaxStreams.setDescription('Maximum number of streams supported.The default value is 128. @Config(config=yes, reboot=yes) ')
bcsSimScsEcmgRedundancyConfigApplyTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4), )
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyTable.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyTable.setDescription('Table of Apply Change for the data for bcsSimScsEcmgRedundancyConfigTable. A row of this table corresponds to a row in bcsSimScsEcmgRedundancyConfigTable.')
bcsSimScsEcmgRedundancyConfigApplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgRedundancyConfigApplyIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyEntry.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyEntry.setDescription('ECMG Redundancy Configuration Apply Table Entry.')
bcsSimScsEcmgRedundancyConfigApplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyIndex.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyIndex.setDescription('ECMG index - also maps to the bcsSimScsEcmgRedundancyConfigTable index')
bcsSimScsEcmgRedundancyConfigApplyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1, 2), ApplyDataToDeviceTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyChange.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyChange.setDescription("The Apply for a row of data in bcsSimScsEcmgRedundancyConfigTable. A row in this table corresponds to the same row index in the bcsSimScsEcmgRedundancyConfigTable. This parameter MUST be set to 'apply' in order for any of the data in the rows to take effect in the SEM. This parameter MUST be set LAST after all other data in the configuration table rows has been configured. @Config(config=no, reboot=no)")
bcsSimScsMibSupportStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notCapable", 1), ("capable", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMibSupportStatus.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsMibSupportStatus.setDescription('Indicates whether the device is capable of supporting and/or enabled to support the functionality of the bcsSimulcryptScs MIB.')
bcsSimScsMaxEcmg = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMaxEcmg.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsMaxEcmg.setDescription('The maximum number of ECMGs this device can support.')
bcsSimScsMaxPrograms = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMaxPrograms.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsMaxPrograms.setDescription('The maximum number of programs this device can support.')
bcsSimScsMaxProgramEcmg = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMaxProgramEcmg.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsMaxProgramEcmg.setDescription('The maximum number of ECMGs that can be associated with a program in this device.')
bcsSimScsEcmgRedundancyConfigInvalidApplyText = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigInvalidApplyText.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigInvalidApplyText.setDescription("When bcsSimScsEcmgRedundancyConfigApplyChange is set to 'applyNotInProgressInvalidData' this entry may contain a text description of what was wrong with the data. This entry contains the description for the most recent apply of a related entry that was invalid.")
bcsSimScsEcmgStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2), )
if mibBuilder.loadTexts: bcsSimScsEcmgStatusTable.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgStatusTable.setDescription('It contains status information for the SCS to ECMG connections. There can be up to bcsSimScsMaxEcmg active SCS to ECMG connections at a time.')
bcsSimScsEcmgStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgStatusIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgStatusEntry.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgStatusEntry.setDescription('A single entry in the bcsSimScsEcmgStatusTable table.')
bcsSimScsEcmgStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsSimScsEcmgStatusIndex.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgStatusIndex.setDescription('This index is used to traverse the bcsSimScsEcmgTable table. The index varies from 1..bcsSimScsMaxEcmg. In the event that some connections are not active this will be designated by the value of bcsSimScsEcmgChannelState.')
bcsSimScsEcmgTcpState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgTcpState.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgTcpState.setDescription('This column specifies TCP connection state of this SCS <==> ECMG connection.')
bcsSimScsEcmgChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgChannelId.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgChannelId.setDescription('This column specifies channel ID.')
bcsSimScsEcmgChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("notOpen", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgChannelState.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgChannelState.setDescription('This column specifies ECMG channel state of this SCS <==> ECMG connection.')
bcsSimScsEcmgSuperCasId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgSuperCasId.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsEcmgSuperCasId.setDescription('This column specifies super CAS Id of the ECMG that the SCS is connected to on this connection.')
bcsSimScsProgramTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3), )
if mibBuilder.loadTexts: bcsSimScsProgramTable.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramTable.setDescription('It contains status information for the SCS programs. There can be up to bcsSimScsMaxPrograms Simulcrypt programs active in the SCS at a time. Each program can be associated with up to bcsSimScsMaxProgramEcmg.')
bcsSimScsProgramEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsProgramIndex"), (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsProgramEcmgIndex"))
if mibBuilder.loadTexts: bcsSimScsProgramEntry.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramEntry.setDescription('A single entry in the bcsSimScsProgramTable table.')
bcsSimScsProgramIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsSimScsProgramIndex.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramIndex.setDescription('This index is used to traverse the bcsSimScsProgramTable table. Limited by bcsSimScsMaxPrograms.')
bcsSimScsProgramEcmgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: bcsSimScsProgramEcmgIndex.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramEcmgIndex.setDescription('ECMG index. This index is used to traverse the bcsSimScsProgramTable table. Limited by bcsSimScsMaxProgramEcmg.')
bcsSimScsProgramState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noEventRunning", 1), ("eventRunning", 2), ("notConfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramState.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramState.setDescription('This column displays the service state of this program. (1) - program configured, no event running (2) - program configured, event running normally (3) - program not configured')
bcsSimScsProgramCryptoPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramCryptoPeriod.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramCryptoPeriod.setDescription('This column displays the actual crypto-period in seconds that is in use for this program.')
bcsSimScsProgramChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramChannelId.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramChannelId.setDescription('This column displays the channel ID.')
bcsSimScsProgramEcmgSuperCasId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramEcmgSuperCasId.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramEcmgSuperCasId.setDescription('This column displays the Super CAS-ID of the 1st ECMG on this service.')
bcsSimScsProgramEcmgStreamState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("error", 3), ("notConfigured", 4), ("invalidCasId", 5), ("ecmTimeout", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramEcmgStreamState.setStatus('current')
if mibBuilder.loadTexts: bcsSimScsProgramEcmgStreamState.setDescription('This column displays the stream state for an ECMG on this service.')
mibBuilder.exportSymbols("BCSSIMULCRYPTSCS-MIB", bcsSimScsEcmgConnectIpAddr=bcsSimScsEcmgConnectIpAddr, bcsSimScsEcmgRedundancyConfigTable=bcsSimScsEcmgRedundancyConfigTable, bcsSimScsEcmgRedundancyConfigIndex=bcsSimScsEcmgRedundancyConfigIndex, bcsSimScsEcmgRedundancyConfigManualSwitchBack=bcsSimScsEcmgRedundancyConfigManualSwitchBack, bcsSimScsEcmIdInitial=bcsSimScsEcmIdInitial, ApplyDataToDeviceTYPE=ApplyDataToDeviceTYPE, bcsSimScsProgramEntry=bcsSimScsProgramEntry, bcsSimScsProgramEcmgSuperCasId=bcsSimScsProgramEcmgSuperCasId, bcsSimScsEcmgStatusEntry=bcsSimScsEcmgStatusEntry, bcsSimScsProgramIndex=bcsSimScsProgramIndex, bcsSimScsEcmgStatusIndex=bcsSimScsEcmgStatusIndex, bcsSimScsConfigGeneral=bcsSimScsConfigGeneral, bcsSimScsConfig=bcsSimScsConfig, bcsSimScsEcmgConnectPort=bcsSimScsEcmgConnectPort, bcsSimScsAccessCriteriaSource=bcsSimScsAccessCriteriaSource, EnableDisableTYPE=EnableDisableTYPE, bcsSimulcryptScs=bcsSimulcryptScs, bcsSimScsEcmgRedundancyConfigApplyTable=bcsSimScsEcmgRedundancyConfigApplyTable, bcsSimScsEcmgRedundancyConfigAutoSwitchBack=bcsSimScsEcmgRedundancyConfigAutoSwitchBack, bcsSimScsEcmgRedundancyConfigMaxStreams=bcsSimScsEcmgRedundancyConfigMaxStreams, bcsSimScsNetworkId=bcsSimScsNetworkId, bcsSimScsEcmgSuperCasId=bcsSimScsEcmgSuperCasId, bcsSimScsEcmgRedundancyConfigEntry=bcsSimScsEcmgRedundancyConfigEntry, PYSNMP_MODULE_ID=bcsSimulcryptScs, bcsSimScsEcmgStatusTable=bcsSimScsEcmgStatusTable, bcsSimScsEcmgTcpState=bcsSimScsEcmgTcpState, bcsSimScsEcmgRedundancyConfigApplyIndex=bcsSimScsEcmgRedundancyConfigApplyIndex, bcsSimScsEcmgRedundancyConfigInvalidApplyText=bcsSimScsEcmgRedundancyConfigInvalidApplyText, bcsSimScsStatus=bcsSimScsStatus, bcsSimScsEcmgChannelState=bcsSimScsEcmgChannelState, bcsSimScsEcmgChannelId=bcsSimScsEcmgChannelId, bcsSimScsEcmgConnectionEntry=bcsSimScsEcmgConnectionEntry, bcsSimScsEcmgConnectIndex=bcsSimScsEcmgConnectIndex, bcsSimScsEcmgRedundancyConfigApplyEntry=bcsSimScsEcmgRedundancyConfigApplyEntry, bcsSimScsProgramState=bcsSimScsProgramState, bcsSimScsProgramChannelId=bcsSimScsProgramChannelId, bcsSimScsEcmgRedundancyConfigApplyChange=bcsSimScsEcmgRedundancyConfigApplyChange, ManualSwitchBackTYPE=ManualSwitchBackTYPE, bcsSimScsStatusGeneral=bcsSimScsStatusGeneral, bcsSimScsMibSupportStatus=bcsSimScsMibSupportStatus, bcsSimScsNominalCryptoPeriod=bcsSimScsNominalCryptoPeriod, bcsSimScsEcmgTimeout=bcsSimScsEcmgTimeout, bcsSimScsMaxPrograms=bcsSimScsMaxPrograms, bcsSimScsMaxProgramEcmg=bcsSimScsMaxProgramEcmg, bcsSimScsProgramEcmgStreamState=bcsSimScsProgramEcmgStreamState, bcsSimScsEcmReplyTimeout=bcsSimScsEcmReplyTimeout, bcsSimScsEcmChannelTestPeriodicity=bcsSimScsEcmChannelTestPeriodicity, bcsSimScsEcmNetworkDelay=bcsSimScsEcmNetworkDelay, bcsSimScsProgramTable=bcsSimScsProgramTable, bcsSimScsEcmgConnectionTable=bcsSimScsEcmgConnectionTable, bcsSimScsMaxNetworkDelay=bcsSimScsMaxNetworkDelay, bcsSimScsEcmgConnectSuperCasId=bcsSimScsEcmgConnectSuperCasId, bcsSimScsProgramCryptoPeriod=bcsSimScsProgramCryptoPeriod, bcsSimScsProgramEcmgIndex=bcsSimScsProgramEcmgIndex, bcsSimScsMaxEcmg=bcsSimScsMaxEcmg, bcsSimScsEcmgConnectEnabled=bcsSimScsEcmgConnectEnabled)
