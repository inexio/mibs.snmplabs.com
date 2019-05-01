#
# PySNMP MIB module CYAN-PME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-PME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
CyanTypeTc, cyanEntityModules = mibBuilder.importSymbols("CYAN-MIB", "CyanTypeTc", "cyanEntityModules")
CyanSecServiceStateTc, CyanOffOnTc, CyanOpStateQualTc, CyanActvStdbyTc, CyanOpStateTc, CyanLEDTc, CyanAdminStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanSecServiceStateTc", "CyanOffOnTc", "CyanOpStateQualTc", "CyanActvStdbyTc", "CyanOpStateTc", "CyanLEDTc", "CyanAdminStateTc")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, iso, ModuleIdentity, Counter64, Bits, Gauge32, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "iso", "ModuleIdentity", "Counter64", "Bits", "Gauge32", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanPmeModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110))
cyanPmeModule.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanPmeModule.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanPmeModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanPmeModule.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanPmeModule.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanPmeModule.setDescription('MIB module for Packet Multiplexer Element(PME)')
cyanPmeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1))
cyanPmeTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1), )
if mibBuilder.loadTexts: cyanPmeTable.setStatus('current')
if mibBuilder.loadTexts: cyanPmeTable.setDescription('A list of Pme entries.')
cyanPmeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1), ).setIndexNames((0, "CYAN-PME-MIB", "cyanPmeShelfId"), (0, "CYAN-PME-MIB", "cyanPmePmeId"))
if mibBuilder.loadTexts: cyanPmeEntry.setStatus('current')
if mibBuilder.loadTexts: cyanPmeEntry.setDescription('An entry of Pme.')
cyanPmeShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanPmeShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanPmeShelfId.setDescription('Shelf Id')
cyanPmePmeId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanPmePmeId.setStatus('current')
if mibBuilder.loadTexts: cyanPmePmeId.setDescription('PME Module Id')
cyanPmeActiveLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 3), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeActiveLed.setStatus('current')
if mibBuilder.loadTexts: cyanPmeActiveLed.setDescription('Active LED status')
cyanPmeActivestandbyState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 4), CyanActvStdbyTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeActivestandbyState.setStatus('current')
if mibBuilder.loadTexts: cyanPmeActivestandbyState.setDescription('Active/standby state')
cyanPmeAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 5), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeAdminState.setStatus('current')
if mibBuilder.loadTexts: cyanPmeAdminState.setDescription('Administrative state')
cyanPmeAlarmLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 6), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeAlarmLed.setStatus('current')
if mibBuilder.loadTexts: cyanPmeAlarmLed.setDescription('Alarm LED status')
cyanPmeAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 124))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeAssetTag.setStatus('current')
if mibBuilder.loadTexts: cyanPmeAssetTag.setDescription('Asset Tag')
cyanPmeAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeAutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanPmeAutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanPmeBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeBaseMacAddress.setStatus('current')
if mibBuilder.loadTexts: cyanPmeBaseMacAddress.setDescription('Base MAC address of a range of addresses')
cyanPmeCurrCyanSwBuildVersions = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeCurrCyanSwBuildVersions.setStatus('current')
if mibBuilder.loadTexts: cyanPmeCurrCyanSwBuildVersions.setDescription('Current Cyan software build versions')
cyanPmeCurrCyanSwRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeCurrCyanSwRelease.setStatus('current')
if mibBuilder.loadTexts: cyanPmeCurrCyanSwRelease.setDescription('Current Cyan software release')
cyanPmeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeCurrent.setStatus('current')
if mibBuilder.loadTexts: cyanPmeCurrent.setDescription('Current Draw')
cyanPmeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeDescription.setStatus('current')
if mibBuilder.loadTexts: cyanPmeDescription.setDescription('Description')
cyanPmeExhaustAirTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeExhaustAirTemp.setStatus('current')
if mibBuilder.loadTexts: cyanPmeExhaustAirTemp.setDescription('Exhaust air temperature')
cyanPmeExhaustTempAlarmHighThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeExhaustTempAlarmHighThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeExhaustTempAlarmHighThres.setDescription('High alarm threshold for exhaust air temperature')
cyanPmeExhaustTempAlarmLowThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeExhaustTempAlarmLowThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeExhaustTempAlarmLowThres.setDescription('Low alarm threshold for exhaust air temperature')
cyanPmeExhaustTempWarnHighThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeExhaustTempWarnHighThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeExhaustTempWarnHighThres.setDescription('High warning threshold for exhaust air temperature')
cyanPmeExhaustTempWarnLowThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeExhaustTempWarnLowThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeExhaustTempWarnLowThres.setDescription('Low warning threshold for exhaust air temperature')
cyanPmeExpectedTemperatureRise = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeExpectedTemperatureRise.setStatus('current')
if mibBuilder.loadTexts: cyanPmeExpectedTemperatureRise.setDescription('Expected temperature rise')
cyanPmeIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeIdentifier.setStatus('current')
if mibBuilder.loadTexts: cyanPmeIdentifier.setDescription('string OID')
cyanPmeIntakeAirTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeIntakeAirTemp.setStatus('current')
if mibBuilder.loadTexts: cyanPmeIntakeAirTemp.setDescription('In-take air temperature')
cyanPmeIntakeTempAlarmHighThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeIntakeTempAlarmHighThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeIntakeTempAlarmHighThres.setDescription('High alarm threshold for in-take air temperature')
cyanPmeIntakeTempAlarmLowThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeIntakeTempAlarmLowThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeIntakeTempAlarmLowThres.setDescription('Low alarm threshold for in-take air temperature')
cyanPmeIntakeTempWarnHighThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeIntakeTempWarnHighThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeIntakeTempWarnHighThres.setDescription('High warning threshold for in-take air temperature')
cyanPmeIntakeTempWarnLowThres = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128000, 128000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeIntakeTempWarnLowThres.setStatus('current')
if mibBuilder.loadTexts: cyanPmeIntakeTempWarnLowThres.setDescription('Low warning threshold for in-take air temperature')
cyanPmeLedTest = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeLedTest.setStatus('current')
if mibBuilder.loadTexts: cyanPmeLedTest.setDescription('Change value of this attribute to run LED test on this module')
cyanPmeMacBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 27), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMacBlockSize.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMacBlockSize.setDescription('Number of MAC addresses allocated from the base MAC address')
cyanPmeMfgCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMfgCleiCode.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMfgCleiCode.setDescription('Common Language Equipment Identifier')
cyanPmeMfgEciCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMfgEciCode.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMfgEciCode.setDescription('Equipment Catalog Item')
cyanPmeMfgModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 30), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMfgModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMfgModuleId.setDescription('Module ID')
cyanPmeMfgPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMfgPartNumber.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMfgPartNumber.setDescription('Manufacturing part number')
cyanPmeMfgRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMfgRevision.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMfgRevision.setDescription('Mfg revision number')
cyanPmeMfgSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 33), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeMfgSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cyanPmeMfgSerialNumber.setDescription('Mfg serial number')
cyanPmeName = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 34), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeName.setStatus('current')
if mibBuilder.loadTexts: cyanPmeName.setDescription('Cyan name')
cyanPmeOidClass = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 35), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeOidClass.setStatus('current')
if mibBuilder.loadTexts: cyanPmeOidClass.setDescription('OID Class')
cyanPmeOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 36), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeOperState.setStatus('current')
if mibBuilder.loadTexts: cyanPmeOperState.setDescription('Primary Operation State')
cyanPmeOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 37), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeOperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanPmeOperStateQual.setDescription('Operation state qualifier')
cyanPmeOssLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 38), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeOssLabel.setStatus('current')
if mibBuilder.loadTexts: cyanPmeOssLabel.setDescription('CyMS label')
cyanPmeOvervoltageThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeOvervoltageThreshold.setStatus('current')
if mibBuilder.loadTexts: cyanPmeOvervoltageThreshold.setDescription('Over-voltage warning threshold')
cyanPmeOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 40), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeOwner.setStatus('current')
if mibBuilder.loadTexts: cyanPmeOwner.setDescription('Owner')
cyanPmePartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 41), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePartNumber.setStatus('current')
if mibBuilder.loadTexts: cyanPmePartNumber.setDescription('Cyan part number')
cyanPmePowerLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 42), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePowerLed.setStatus('current')
if mibBuilder.loadTexts: cyanPmePowerLed.setDescription('Power LED status')
cyanPmePsuTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 43), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25000, 85000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePsuTemperature.setStatus('current')
if mibBuilder.loadTexts: cyanPmePsuTemperature.setDescription('Temperature reading in the power supply')
cyanPmePwrFeedAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 44), CyanOffOnTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePwrFeedAStatus.setStatus('current')
if mibBuilder.loadTexts: cyanPmePwrFeedAStatus.setDescription('Status of power supply A')
cyanPmePwrFeedAVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePwrFeedAVoltage.setStatus('current')
if mibBuilder.loadTexts: cyanPmePwrFeedAVoltage.setDescription('Voltage level of power supply A')
cyanPmePwrFeedBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 46), CyanOffOnTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePwrFeedBStatus.setStatus('current')
if mibBuilder.loadTexts: cyanPmePwrFeedBStatus.setDescription('Status of power supply B')
cyanPmePwrFeedBVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmePwrFeedBVoltage.setStatus('current')
if mibBuilder.loadTexts: cyanPmePwrFeedBVoltage.setDescription('Voltage level of power supply B')
cyanPmeResendEthlinkoamPdus = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 48), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeResendEthlinkoamPdus.setStatus('current')
if mibBuilder.loadTexts: cyanPmeResendEthlinkoamPdus.setDescription('802.3ah Clause 57 link OAM event resend count')
cyanPmeRevertCyanSwBuildVersions = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 49), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeRevertCyanSwBuildVersions.setStatus('current')
if mibBuilder.loadTexts: cyanPmeRevertCyanSwBuildVersions.setDescription('Revert Cyan software build versions')
cyanPmeRevertCyanSwRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 50), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeRevertCyanSwRelease.setStatus('current')
if mibBuilder.loadTexts: cyanPmeRevertCyanSwRelease.setDescription('Revert Cyan software release')
cyanPmeSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 51), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeSecServState.setStatus('current')
if mibBuilder.loadTexts: cyanPmeSecServState.setDescription('Secondary service state')
cyanPmeSynchLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 52), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeSynchLed.setStatus('current')
if mibBuilder.loadTexts: cyanPmeSynchLed.setDescription('Synch LED status')
cyanPmeType = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 53), CyanTypeTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeType.setStatus('current')
if mibBuilder.loadTexts: cyanPmeType.setDescription('Equipment type')
cyanPmeUndervoltageThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeUndervoltageThreshold.setStatus('current')
if mibBuilder.loadTexts: cyanPmeUndervoltageThreshold.setDescription('Under-voltage warning threshold')
cyanPmeUpgradeCyanSwBuildVersions = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 55), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeUpgradeCyanSwBuildVersions.setStatus('current')
if mibBuilder.loadTexts: cyanPmeUpgradeCyanSwBuildVersions.setDescription('Upgrade Cyan software build versions')
cyanPmeUpgradeCyanSwRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 1, 1, 1, 56), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanPmeUpgradeCyanSwRelease.setStatus('current')
if mibBuilder.loadTexts: cyanPmeUpgradeCyanSwRelease.setDescription('Upgrade Cyan software release')
cyanPmeObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 20)).setObjects(("CYAN-PME-MIB", "cyanPmeActiveLed"), ("CYAN-PME-MIB", "cyanPmeActivestandbyState"), ("CYAN-PME-MIB", "cyanPmeAdminState"), ("CYAN-PME-MIB", "cyanPmeAlarmLed"), ("CYAN-PME-MIB", "cyanPmeAssetTag"), ("CYAN-PME-MIB", "cyanPmeAutoinserviceSoakTimeSec"), ("CYAN-PME-MIB", "cyanPmeBaseMacAddress"), ("CYAN-PME-MIB", "cyanPmeCurrCyanSwBuildVersions"), ("CYAN-PME-MIB", "cyanPmeCurrCyanSwRelease"), ("CYAN-PME-MIB", "cyanPmeCurrent"), ("CYAN-PME-MIB", "cyanPmeDescription"), ("CYAN-PME-MIB", "cyanPmeExhaustAirTemp"), ("CYAN-PME-MIB", "cyanPmeExhaustTempAlarmHighThres"), ("CYAN-PME-MIB", "cyanPmeExhaustTempAlarmLowThres"), ("CYAN-PME-MIB", "cyanPmeExhaustTempWarnHighThres"), ("CYAN-PME-MIB", "cyanPmeExhaustTempWarnLowThres"), ("CYAN-PME-MIB", "cyanPmeExpectedTemperatureRise"), ("CYAN-PME-MIB", "cyanPmeIdentifier"), ("CYAN-PME-MIB", "cyanPmeIntakeAirTemp"), ("CYAN-PME-MIB", "cyanPmeIntakeTempAlarmHighThres"), ("CYAN-PME-MIB", "cyanPmeIntakeTempAlarmLowThres"), ("CYAN-PME-MIB", "cyanPmeIntakeTempWarnHighThres"), ("CYAN-PME-MIB", "cyanPmeIntakeTempWarnLowThres"), ("CYAN-PME-MIB", "cyanPmeLedTest"), ("CYAN-PME-MIB", "cyanPmeMacBlockSize"), ("CYAN-PME-MIB", "cyanPmeMfgCleiCode"), ("CYAN-PME-MIB", "cyanPmeMfgEciCode"), ("CYAN-PME-MIB", "cyanPmeMfgModuleId"), ("CYAN-PME-MIB", "cyanPmeMfgPartNumber"), ("CYAN-PME-MIB", "cyanPmeMfgRevision"), ("CYAN-PME-MIB", "cyanPmeMfgSerialNumber"), ("CYAN-PME-MIB", "cyanPmeName"), ("CYAN-PME-MIB", "cyanPmeOidClass"), ("CYAN-PME-MIB", "cyanPmeOperState"), ("CYAN-PME-MIB", "cyanPmeOperStateQual"), ("CYAN-PME-MIB", "cyanPmeOssLabel"), ("CYAN-PME-MIB", "cyanPmeOvervoltageThreshold"), ("CYAN-PME-MIB", "cyanPmeOwner"), ("CYAN-PME-MIB", "cyanPmePartNumber"), ("CYAN-PME-MIB", "cyanPmePowerLed"), ("CYAN-PME-MIB", "cyanPmePsuTemperature"), ("CYAN-PME-MIB", "cyanPmePwrFeedAStatus"), ("CYAN-PME-MIB", "cyanPmePwrFeedAVoltage"), ("CYAN-PME-MIB", "cyanPmePwrFeedBStatus"), ("CYAN-PME-MIB", "cyanPmePwrFeedBVoltage"), ("CYAN-PME-MIB", "cyanPmeResendEthlinkoamPdus"), ("CYAN-PME-MIB", "cyanPmeRevertCyanSwBuildVersions"), ("CYAN-PME-MIB", "cyanPmeRevertCyanSwRelease"), ("CYAN-PME-MIB", "cyanPmeSecServState"), ("CYAN-PME-MIB", "cyanPmeSynchLed"), ("CYAN-PME-MIB", "cyanPmeType"), ("CYAN-PME-MIB", "cyanPmeUndervoltageThreshold"), ("CYAN-PME-MIB", "cyanPmeUpgradeCyanSwBuildVersions"), ("CYAN-PME-MIB", "cyanPmeUpgradeCyanSwRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanPmeObjectGroup = cyanPmeObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanPmeObjectGroup.setDescription('Group of objects that comes with Pme module')
cyanPmeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 110, 30)).setObjects(("CYAN-PME-MIB", "cyanPmeObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanPmeCompliance = cyanPmeCompliance.setStatus('current')
if mibBuilder.loadTexts: cyanPmeCompliance.setDescription('The basic info needed to be a cyan Pme')
mibBuilder.exportSymbols("CYAN-PME-MIB", cyanPmeIntakeTempAlarmHighThres=cyanPmeIntakeTempAlarmHighThres, cyanPmePwrFeedAStatus=cyanPmePwrFeedAStatus, cyanPmeTable=cyanPmeTable, cyanPmeUpgradeCyanSwRelease=cyanPmeUpgradeCyanSwRelease, cyanPmeSynchLed=cyanPmeSynchLed, cyanPmePwrFeedBVoltage=cyanPmePwrFeedBVoltage, PYSNMP_MODULE_ID=cyanPmeModule, cyanPmeEntry=cyanPmeEntry, cyanPmeOwner=cyanPmeOwner, cyanPmeOperState=cyanPmeOperState, cyanPmePsuTemperature=cyanPmePsuTemperature, cyanPmeRevertCyanSwRelease=cyanPmeRevertCyanSwRelease, cyanPmeLedTest=cyanPmeLedTest, cyanPmeExhaustTempAlarmLowThres=cyanPmeExhaustTempAlarmLowThres, cyanPmeSecServState=cyanPmeSecServState, cyanPmePwrFeedBStatus=cyanPmePwrFeedBStatus, cyanPmePmeId=cyanPmePmeId, cyanPmeOvervoltageThreshold=cyanPmeOvervoltageThreshold, cyanPmePartNumber=cyanPmePartNumber, cyanPmeRevertCyanSwBuildVersions=cyanPmeRevertCyanSwBuildVersions, cyanPmeAdminState=cyanPmeAdminState, cyanPmeOssLabel=cyanPmeOssLabel, cyanPmeMfgRevision=cyanPmeMfgRevision, cyanPmeIntakeTempWarnLowThres=cyanPmeIntakeTempWarnLowThres, cyanPmeExhaustTempAlarmHighThres=cyanPmeExhaustTempAlarmHighThres, cyanPmeMfgCleiCode=cyanPmeMfgCleiCode, cyanPmeUpgradeCyanSwBuildVersions=cyanPmeUpgradeCyanSwBuildVersions, cyanPmeIntakeTempWarnHighThres=cyanPmeIntakeTempWarnHighThres, cyanPmeMacBlockSize=cyanPmeMacBlockSize, cyanPmeActiveLed=cyanPmeActiveLed, cyanPmeShelfId=cyanPmeShelfId, cyanPmeIntakeTempAlarmLowThres=cyanPmeIntakeTempAlarmLowThres, cyanPmeMfgModuleId=cyanPmeMfgModuleId, cyanPmeOperStateQual=cyanPmeOperStateQual, cyanPmeCurrCyanSwRelease=cyanPmeCurrCyanSwRelease, cyanPmeResendEthlinkoamPdus=cyanPmeResendEthlinkoamPdus, cyanPmeAlarmLed=cyanPmeAlarmLed, cyanPmeCompliance=cyanPmeCompliance, cyanPmeExhaustTempWarnHighThres=cyanPmeExhaustTempWarnHighThres, cyanPmeExpectedTemperatureRise=cyanPmeExpectedTemperatureRise, cyanPmeMfgSerialNumber=cyanPmeMfgSerialNumber, cyanPmeModule=cyanPmeModule, cyanPmeExhaustAirTemp=cyanPmeExhaustAirTemp, cyanPmeActivestandbyState=cyanPmeActivestandbyState, cyanPmeExhaustTempWarnLowThres=cyanPmeExhaustTempWarnLowThres, cyanPmeDescription=cyanPmeDescription, cyanPmeIdentifier=cyanPmeIdentifier, cyanPmeMfgEciCode=cyanPmeMfgEciCode, cyanPmeName=cyanPmeName, cyanPmePwrFeedAVoltage=cyanPmePwrFeedAVoltage, cyanPmeObjectGroup=cyanPmeObjectGroup, cyanPmeCurrCyanSwBuildVersions=cyanPmeCurrCyanSwBuildVersions, cyanPmeMfgPartNumber=cyanPmeMfgPartNumber, cyanPmeMibObjects=cyanPmeMibObjects, cyanPmeBaseMacAddress=cyanPmeBaseMacAddress, cyanPmeIntakeAirTemp=cyanPmeIntakeAirTemp, cyanPmeUndervoltageThreshold=cyanPmeUndervoltageThreshold, cyanPmeOidClass=cyanPmeOidClass, cyanPmeType=cyanPmeType, cyanPmePowerLed=cyanPmePowerLed, cyanPmeCurrent=cyanPmeCurrent, cyanPmeAssetTag=cyanPmeAssetTag, cyanPmeAutoinserviceSoakTimeSec=cyanPmeAutoinserviceSoakTimeSec)
