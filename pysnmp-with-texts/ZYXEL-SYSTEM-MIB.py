#
# PySNMP MIB module ZYXEL-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ModuleIdentity, IpAddress, Integer32, Unsigned32, TimeTicks, ObjectIdentity, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ModuleIdentity", "IpAddress", "Integer32", "Unsigned32", "TimeTicks", "ObjectIdentity", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82))
if mibBuilder.loadTexts: zyxelSystem.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelSystem.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelSystem.setContactInfo('')
if mibBuilder.loadTexts: zyxelSystem.setDescription('The subtree for system')
zyxelDateTimeSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1))
zyxelSysInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2))
zyxelDateTimeTrapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 3))
zyDateTimeServerType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("daytime", 2), ("time", 3), ("ntp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeServerType.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeServerType.setDescription('The time service protocol that your timeserver uses.')
zyDateTimeServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeServerIpAddress.setDescription('IP address of time server.')
zyDateTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeZone.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeZone.setDescription('The time difference between UTC and your time zone. Ex: +01')
zyDateTimeNewDateYear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeNewDateYear.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeNewDateYear.setDescription('The new date in year.')
zyDateTimeNewDateMonth = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeNewDateMonth.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeNewDateMonth.setDescription('The new date in month.')
zyDateTimeNewDateDay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeNewDateDay.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeNewDateDay.setDescription('The new date in day.')
zyDateTimeNewTimeHour = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeNewTimeHour.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeNewTimeHour.setDescription('The new time in hour.')
zyDateTimeNewTimeMinute = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeNewTimeMinute.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeNewTimeMinute.setDescription('The new time in minute.')
zyDateTimeNewTimeSecond = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDateTimeNewTimeSecond.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeNewTimeSecond.setDescription('The new time in second.')
zyxelDateTimeDaylightSavingTimeSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10))
zyDaylightSavingTimeState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeState.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeState.setDescription('Enable/Disable Daylight Saving Time service for the switch. Daylight saving is a period from late spring to early fall when many countries set their clocks ahead of normal local time by one hour to give more daytime light in the evening.')
zyDaylightSavingTimeStartDateWeek = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("first", 1), ("second", 2), ("third", 3), ("fourth", 4), ("last", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateWeek.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateWeek.setDescription('Start week of Daylight Saving Time service.')
zyDaylightSavingTimeStartDateDay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateDay.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateDay.setDescription('Start day of Daylight Saving Time service.')
zyDaylightSavingTimeStartDateMonth = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("january", 1), ("february", 2), ("march", 3), ("april", 4), ("may", 5), ("june", 6), ("july", 7), ("august", 8), ("september", 9), ("october", 10), ("november", 11), ("december", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateMonth.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateMonth.setDescription('Start month of Daylight Saving Time service.')
zyDaylightSavingTimeStartDateHour = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateHour.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeStartDateHour.setDescription('Start time of Daylight Saving Time service.')
zyDaylightSavingTimeEndDateWeek = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("first", 1), ("second", 2), ("third", 3), ("fourth", 4), ("last", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateWeek.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateWeek.setDescription('End week of Daylight Saving Time service.')
zyDaylightSavingTimeEndDateDay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateDay.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateDay.setDescription('End day of Daylight Saving Time service.')
zyDaylightSavingTimeEndDateMonth = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("january", 1), ("february", 2), ("march", 3), ("april", 4), ("may", 5), ("june", 6), ("july", 7), ("august", 8), ("september", 9), ("october", 10), ("november", 11), ("december", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateMonth.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateMonth.setDescription('End month of Daylight Saving Time service.')
zyDaylightSavingTimeEndDateHour = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateHour.setStatus('current')
if mibBuilder.loadTexts: zyDaylightSavingTimeEndDateHour.setDescription('End time of Daylight Saving Time service.')
zySysSwPlatformMajorVers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwPlatformMajorVers.setStatus('current')
if mibBuilder.loadTexts: zySysSwPlatformMajorVers.setDescription('Software platform major version, e.g. 3.')
zySysSwPlatformMinorVers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwPlatformMinorVers.setStatus('current')
if mibBuilder.loadTexts: zySysSwPlatformMinorVers.setDescription('Software platform minor version, e.g. 50.')
zySysSwModelString = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwModelString.setStatus('current')
if mibBuilder.loadTexts: zySysSwModelString.setDescription('Software model letters, e.g. TJ.')
zySysSwVersionControlNbr = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwVersionControlNbr.setStatus('current')
if mibBuilder.loadTexts: zySysSwVersionControlNbr.setDescription('Software version control number, e.g. 0.')
zySysSwDay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwDay.setStatus('current')
if mibBuilder.loadTexts: zySysSwDay.setDescription('Software compilation day, e.g. 19.')
zySysSwMonth = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwMonth.setStatus('current')
if mibBuilder.loadTexts: zySysSwMonth.setDescription('Software compilation month, e.g. 8.')
zySysSwYear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwYear.setStatus('current')
if mibBuilder.loadTexts: zySysSwYear.setDescription('Software compilation year, e.g. 2004.')
zySysHwMajorVers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysHwMajorVers.setStatus('current')
if mibBuilder.loadTexts: zySysHwMajorVers.setDescription('Hardware major version, e.g. 1.')
zySysHwMinorVers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysHwMinorVers.setStatus('current')
if mibBuilder.loadTexts: zySysHwMinorVers.setDescription('Hardware minor version, e.g. 0.')
zySysSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSerialNumber.setStatus('current')
if mibBuilder.loadTexts: zySysSerialNumber.setDescription('Serial number.')
zySysSwBootUpImage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("image1", 1), ("image2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysSwBootUpImage.setStatus('current')
if mibBuilder.loadTexts: zySysSwBootUpImage.setDescription('Current system boot up image. You can change the boot up image of next rebooting by setting sysMgmtBootupImage.')
zyDateTimeTrapTimeServerNotReachable = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 3, 1))
if mibBuilder.loadTexts: zyDateTimeTrapTimeServerNotReachable.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeTrapTimeServerNotReachable.setDescription('Real time clock is not up to date. It has not been configured manually or time server is unreachable.')
zyDateTimeTrapTimeServerNotReachableRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 3, 2))
if mibBuilder.loadTexts: zyDateTimeTrapTimeServerNotReachableRecovered.setStatus('current')
if mibBuilder.loadTexts: zyDateTimeTrapTimeServerNotReachableRecovered.setDescription('Real time clock is up to date.')
mibBuilder.exportSymbols("ZYXEL-SYSTEM-MIB", PYSNMP_MODULE_ID=zyxelSystem, zyxelSysInfo=zyxelSysInfo, zySysSwBootUpImage=zySysSwBootUpImage, zyDaylightSavingTimeState=zyDaylightSavingTimeState, zyxelDateTimeDaylightSavingTimeSetup=zyxelDateTimeDaylightSavingTimeSetup, zySysSwDay=zySysSwDay, zyDateTimeNewDateMonth=zyDateTimeNewDateMonth, zyDaylightSavingTimeEndDateHour=zyDaylightSavingTimeEndDateHour, zyDaylightSavingTimeEndDateDay=zyDaylightSavingTimeEndDateDay, zyDateTimeNewTimeSecond=zyDateTimeNewTimeSecond, zyDateTimeNewDateYear=zyDateTimeNewDateYear, zyDateTimeServerIpAddress=zyDateTimeServerIpAddress, zySysSwMonth=zySysSwMonth, zyDateTimeTrapTimeServerNotReachableRecovered=zyDateTimeTrapTimeServerNotReachableRecovered, zySysSwYear=zySysSwYear, zyDaylightSavingTimeStartDateDay=zyDaylightSavingTimeStartDateDay, zyxelSystem=zyxelSystem, zyDaylightSavingTimeStartDateHour=zyDaylightSavingTimeStartDateHour, zySysSerialNumber=zySysSerialNumber, zyDaylightSavingTimeEndDateWeek=zyDaylightSavingTimeEndDateWeek, zyDateTimeTrapTimeServerNotReachable=zyDateTimeTrapTimeServerNotReachable, zySysSwVersionControlNbr=zySysSwVersionControlNbr, zySysSwModelString=zySysSwModelString, zySysHwMinorVers=zySysHwMinorVers, zyDateTimeZone=zyDateTimeZone, zyDateTimeNewDateDay=zyDateTimeNewDateDay, zyDaylightSavingTimeEndDateMonth=zyDaylightSavingTimeEndDateMonth, zySysSwPlatformMajorVers=zySysSwPlatformMajorVers, zyDateTimeNewTimeHour=zyDateTimeNewTimeHour, zyDaylightSavingTimeStartDateMonth=zyDaylightSavingTimeStartDateMonth, zySysHwMajorVers=zySysHwMajorVers, zyDaylightSavingTimeStartDateWeek=zyDaylightSavingTimeStartDateWeek, zyxelDateTimeSetup=zyxelDateTimeSetup, zySysSwPlatformMinorVers=zySysSwPlatformMinorVers, zyxelDateTimeTrapNotifications=zyxelDateTimeTrapNotifications, zyDateTimeServerType=zyDateTimeServerType, zyDateTimeNewTimeMinute=zyDateTimeNewTimeMinute)
