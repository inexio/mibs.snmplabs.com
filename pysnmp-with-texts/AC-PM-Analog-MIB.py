#
# PySNMP MIB module AC-PM-Analog-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AC-PM-Analog-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:09:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
acRegistrations, acBoardMibs, acProducts, acGeneric, audioCodes, acPerformance = mibBuilder.importSymbols("AUDIOCODES-TYPES-MIB", "acRegistrations", "acBoardMibs", "acProducts", "acGeneric", "audioCodes", "acPerformance")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Gauge32, MibIdentifier, Counter32, iso, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, enterprises, Bits, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "Counter32", "iso", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "enterprises", "Bits", "NotificationType", "Unsigned32")
DisplayString, TAddress, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TAddress", "DateAndTime", "TextualConvention")
acPMAnalog = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 10, 9))
if mibBuilder.loadTexts: acPMAnalog.setLastUpdated('200611-01926Z')
if mibBuilder.loadTexts: acPMAnalog.setOrganization('AudioCodes Ltd')
if mibBuilder.loadTexts: acPMAnalog.setContactInfo('Postal: Support AudioCodes LTD 1 Hayarden Street Airport City Lod, ISRAEL 70151 Tel: 972-3-9764000 Fax: 972-3-9764040 Email: support@audiocodes.com Web: www.audiocodes.com')
if mibBuilder.loadTexts: acPMAnalog.setDescription("The AC-PM-Analog MIB offers performance monitoring For the Analog related elements in Audiocodes' devices. The Configuration sub-tree is for configuring the interval Period length for the entire AC-PM-Analog MIB, and the different tables' thresholds. The Data sub-tree presents the tables of monitored elements. Note - for the entire MIB the value (-1) means the value Asked for is either not supported or currently not relevant (this is for when values asked for are for intervals not yet recorded.")
acPMAnalogConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 9, 1))
acPMAnalogConfigurationPeriodLength = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 894780))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAnalogConfigurationPeriodLength.setStatus('current')
if mibBuilder.loadTexts: acPMAnalogConfigurationPeriodLength.setDescription('Length of monitoring intervals for entire MIB. Time is in minutes.')
acPMAnalogConfigurationResetTotalCounters = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("resetCountersDone", 1), ("resetTotalCounters", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAnalogConfigurationResetTotalCounters.setStatus('current')
if mibBuilder.loadTexts: acPMAnalogConfigurationResetTotalCounters.setDescription('Total-Counters Reset. To reset the total counters, set the value of this object to resetTotalCounters(2).')
acPMAnalogUtilsAttributes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 31))
acPMAnalogUtilsAttributesOffHookChannelsHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 31, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAnalogUtilsAttributesOffHookChannelsHighThreshold.setStatus('current')
if mibBuilder.loadTexts: acPMAnalogUtilsAttributesOffHookChannelsHighThreshold.setDescription('High threshold.')
acPMAnalogUtilsAttributesOffHookChannelsLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 9, 1, 31, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAnalogUtilsAttributesOffHookChannelsLowThreshold.setStatus('current')
if mibBuilder.loadTexts: acPMAnalogUtilsAttributesOffHookChannelsLowThreshold.setDescription('Low threshold.')
acPMAnalogData = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2))
acPMAnalogDataAcPMAnalogTimeFromStartOfInterval = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAnalogDataAcPMAnalogTimeFromStartOfInterval.setStatus('current')
if mibBuilder.loadTexts: acPMAnalogDataAcPMAnalogTimeFromStartOfInterval.setDescription('The time in seconds since the start of the current interval. MIB specific.')
acPMAnalogUtils = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31))
acPMOffHookChannelsTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21), )
if mibBuilder.loadTexts: acPMOffHookChannelsTable.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsTable.setDescription('Number of active (off-hook) analog lines.')
acPMOffHookChannelsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1), ).setIndexNames((0, "AC-PM-Analog-MIB", "acPMOffHookChannelsInterval"))
if mibBuilder.loadTexts: acPMOffHookChannelsEntry.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsEntry.setDescription('')
acPMOffHookChannelsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMOffHookChannelsInterval.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsInterval.setDescription('Interval index. 0 - current period (incomplete monitoring - mid period). 1 - Last full period. 2 - One before last.')
acPMOffHookChannelsVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsVal.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsVal.setDescription('Value of gauge or counter.')
acPMOffHookChannelsAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsAverage.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsAverage.setDescription('Average value with in the period time.')
acPMOffHookChannelsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsMax.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsMax.setDescription('Maximum value with in the period time.')
acPMOffHookChannelsMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsMin.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsMin.setDescription('Minimum value with in the period time.')
acPMOffHookChannelsVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsVolume.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsVolume.setDescription('Activity volume.')
acPMOffHookChannelsTimeBelowLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsTimeBelowLowThreshold.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsTimeBelowLowThreshold.setDescription('Percent of interval time for which gauge is below what was determined as the low threshold.')
acPMOffHookChannelsTimeBetweenThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsTimeBetweenThresholds.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsTimeBetweenThresholds.setDescription('Percent of interval time for which gauge is above what was determined as the high threshold.')
acPMOffHookChannelsTimeAboveHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsTimeAboveHighThreshold.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsTimeAboveHighThreshold.setDescription('Percent of interval time for which gauge is between what were determined as the low and high thresholds.')
acPMOffHookChannelsFullDayAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 9, 2, 31, 21, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMOffHookChannelsFullDayAverage.setStatus('current')
if mibBuilder.loadTexts: acPMOffHookChannelsFullDayAverage.setDescription('The average of full 24 hours.')
mibBuilder.exportSymbols("AC-PM-Analog-MIB", acPMOffHookChannelsTimeBetweenThresholds=acPMOffHookChannelsTimeBetweenThresholds, acPMOffHookChannelsVal=acPMOffHookChannelsVal, acPMOffHookChannelsTimeBelowLowThreshold=acPMOffHookChannelsTimeBelowLowThreshold, acPMOffHookChannelsMin=acPMOffHookChannelsMin, PYSNMP_MODULE_ID=acPMAnalog, acPMOffHookChannelsTable=acPMOffHookChannelsTable, acPMOffHookChannelsFullDayAverage=acPMOffHookChannelsFullDayAverage, acPMOffHookChannelsTimeAboveHighThreshold=acPMOffHookChannelsTimeAboveHighThreshold, acPMOffHookChannelsAverage=acPMOffHookChannelsAverage, acPMOffHookChannelsEntry=acPMOffHookChannelsEntry, acPMAnalogUtilsAttributesOffHookChannelsLowThreshold=acPMAnalogUtilsAttributesOffHookChannelsLowThreshold, acPMAnalogConfigurationResetTotalCounters=acPMAnalogConfigurationResetTotalCounters, acPMAnalog=acPMAnalog, acPMAnalogConfigurationPeriodLength=acPMAnalogConfigurationPeriodLength, acPMAnalogUtilsAttributes=acPMAnalogUtilsAttributes, acPMAnalogUtilsAttributesOffHookChannelsHighThreshold=acPMAnalogUtilsAttributesOffHookChannelsHighThreshold, acPMAnalogUtils=acPMAnalogUtils, acPMOffHookChannelsMax=acPMOffHookChannelsMax, acPMAnalogDataAcPMAnalogTimeFromStartOfInterval=acPMAnalogDataAcPMAnalogTimeFromStartOfInterval, acPMOffHookChannelsVolume=acPMOffHookChannelsVolume, acPMOffHookChannelsInterval=acPMOffHookChannelsInterval, acPMAnalogData=acPMAnalogData, acPMAnalogConfiguration=acPMAnalogConfiguration)
