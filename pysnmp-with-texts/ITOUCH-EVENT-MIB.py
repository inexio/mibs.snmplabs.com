#
# PySNMP MIB module ITOUCH-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-EVENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:57:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
DateTime, iTouch = mibBuilder.importSymbols("ITOUCH-MIB", "DateTime", "iTouch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, TimeTicks, Unsigned32, Bits, ModuleIdentity, MibIdentifier, Integer32, Counter32, IpAddress, Gauge32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "TimeTicks", "Unsigned32", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32", "Counter32", "IpAddress", "Gauge32", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 33))
class EventGroup(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58))
    namedValues = NamedValues(("appleTalk", 1), ("appleTalkArps", 2), ("appleTalkRtmp", 3), ("appleTalkZip", 4), ("appleTalkNbp", 5), ("appleTalkTraffic", 6), ("atm", 7), ("backup", 8), ("pcmcia", 9), ("chassis", 10), ("circuit", 11), ("clns", 12), ("decNet", 13), ("decNetTraffic", 14), ("egp", 15), ("esis", 16), ("fddi", 17), ("fddiTraffic", 18), ("frame", 19), ("frameRelay", 20), ("hubManagement", 21), ("interface", 22), ("ip", 23), ("ipRip", 24), ("ipRoutes", 25), ("ipTraffic", 26), ("ipx", 27), ("ipxRip", 28), ("ipxSap", 29), ("isdn", 30), ("isdnQ931", 31), ("isdnTrace", 32), ("isis", 33), ("isisHello", 34), ("isisLsp", 35), ("link", 36), ("lmb", 37), ("lqm", 38), ("ospf", 39), ("ospfHello", 40), ("ospfLsaPacket", 41), ("ospfSpf", 42), ("param", 43), ("ppp", 44), ("session", 45), ("spanningTree", 46), ("snmp", 47), ("switchForwarding", 48), ("switchLoopDetect", 49), ("switchManagement", 50), ("system", 51), ("tcp", 52), ("time", 53), ("tokenRingManagement", 54), ("udp", 55), ("ui", 56), ("vlmp", 57), ("x25", 58))

eventTableSize = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 800)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventTableSize.setStatus('mandatory')
if mibBuilder.loadTexts: eventTableSize.setDescription('Controls the size of the event table in number of entries. Event storage begins with entry number one and continues to the upper bound. When the table becomes full, event storeage begins again with entry number one, overwriting the previously stored entry. A newly defined table size will not take effect until the unit is reinitialized.')
eventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discard", 1), ("low", 2), ("medium", 3), ("high", 4))).clone('low')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: eventSeverity.setDescription('The severity of the event to be logged. All events fall into one of the above severity levels. Events are added to the event table if and only if the current value of this object is less than or equal to the severity of the event. If this object is set to discard, no events are logged to the table.')
eventTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("date", 2), ("time", 3), ("datetime", 4))).clone('datetime')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: eventTimestamp.setDescription('This object controls the timestamp embedded into the actual text of the event for event table text object eventTextText. If this object is set to none, no timestamp will be embedded in the text. This object has no effect on the event table text object eventTextDateTime.')
eventLanguage = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("english", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLanguage.setStatus('mandatory')
if mibBuilder.loadTexts: eventLanguage.setDescription('This object indicates the language of the event text in the table.')
eventClearLog = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventClearLog.setStatus('mandatory')
if mibBuilder.loadTexts: eventClearLog.setDescription('When this object is set to execute, all events are cleared from the event table. Setting this object to ready has no effect.')
eventEnableAll = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventEnableAll.setStatus('mandatory')
if mibBuilder.loadTexts: eventEnableAll.setDescription('When this object is set to execute, all events groups are enabled. Setting this object to ready has no effect.')
eventDisableAll = MibScalar((1, 3, 6, 1, 4, 1, 33, 33, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventDisableAll.setStatus('mandatory')
if mibBuilder.loadTexts: eventDisableAll.setDescription('When this object is set to execute, all events groups are disabled. Setting this object to ready has no effect.')
eventGroupTable = MibTable((1, 3, 6, 1, 4, 1, 33, 33, 8), )
if mibBuilder.loadTexts: eventGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: eventGroupTable.setDescription('Table of descriptive and status information about event groups.')
eventGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 33, 8, 1), ).setIndexNames((0, "ITOUCH-EVENT-MIB", "eventGroupIndex"))
if mibBuilder.loadTexts: eventGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: eventGroupEntry.setDescription('An entry in the table, containing information about an event group.')
eventGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 8, 1, 1), EventGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventGroupIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eventGroupIndex.setDescription('This variable identifies the event group.')
eventGroupState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventGroupState.setStatus('mandatory')
if mibBuilder.loadTexts: eventGroupState.setDescription('This variable controls whether events from a particular event group may be logged to the event table.')
eventTextTable = MibTable((1, 3, 6, 1, 4, 1, 33, 33, 9), )
if mibBuilder.loadTexts: eventTextTable.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextTable.setDescription('Table of descriptive and status information about an event.')
eventTextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 33, 9, 1), ).setIndexNames((0, "ITOUCH-EVENT-MIB", "eventTextGroupIndex"), (0, "ITOUCH-EVENT-MIB", "eventTextEventIndex"))
if mibBuilder.loadTexts: eventTextEntry.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextEntry.setDescription('An entry in the table, containing information about an event.')
eventTextGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 1), EventGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTextGroupIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextGroupIndex.setDescription('This variable identifies the event group.')
eventTextEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTextEventIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextEventIndex.setDescription('This variable identifies the event of the desired group. This number is arbitrary, and translates to nth event of the specified group. This value wraps at the 32 bit maximum.')
eventTextText = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTextText.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextText.setDescription('The text of the event in the language defined by eventLanguage.')
eventTextDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 4), DateTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTextDateTime.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextDateTime.setDescription('The timestamp of when the event was posted.')
eventTextSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("low", 2), ("medium", 3), ("high", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTextSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: eventTextSeverity.setDescription('The severity of the event.')
mibBuilder.exportSymbols("ITOUCH-EVENT-MIB", eventTextDateTime=eventTextDateTime, eventGroupEntry=eventGroupEntry, eventSeverity=eventSeverity, eventTextText=eventTextText, eventTextTable=eventTextTable, eventTextSeverity=eventTextSeverity, eventLanguage=eventLanguage, EventGroup=EventGroup, eventGroupIndex=eventGroupIndex, eventGroupState=eventGroupState, eventTextEventIndex=eventTextEventIndex, eventTextEntry=eventTextEntry, eventTableSize=eventTableSize, eventClearLog=eventClearLog, eventGroupTable=eventGroupTable, eventTextGroupIndex=eventTextGroupIndex, xEvent=xEvent, eventDisableAll=eventDisableAll, eventEnableAll=eventEnableAll, eventTimestamp=eventTimestamp)
