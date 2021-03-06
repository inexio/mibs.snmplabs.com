#
# PySNMP MIB module CTRON-DLSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-DLSW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ctDLSW, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDLSW")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Unsigned32, MibIdentifier, NotificationType, Integer32, Counter64, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class NBName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

ctdlswNode = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1))
ctdlswNodeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1))
ctdlswPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2))
ctdlswFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3))
ctdlswTConn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4))
ctdlswTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 5))
ctdlswEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6))
ctdlswEventLogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1))
ctdlswEventLogFilterTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2))
ctdlswEventLogTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3))
ctdlswVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswVersion.setStatus('mandatory')
ctdlswAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswAdminStatus.setStatus('mandatory')
ctdlswOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswOperStatus.setStatus('mandatory')
ctdlswUpTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswUpTime.setStatus('mandatory')
ctdlswOperVirtualRingNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswOperVirtualRingNumber.setStatus('mandatory')
ctdlswNBLocalFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswNBLocalFilterType.setStatus('mandatory')
ctdlswNBRemoteFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswNBRemoteFilterType.setStatus('mandatory')
ctdlswMacLocalFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswMacLocalFilterType.setStatus('mandatory')
ctdlswMacRemoteFilterType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("pass", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswMacRemoteFilterType.setStatus('mandatory')
ctdlswAcceptDynamicTConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswAcceptDynamicTConn.setStatus('mandatory')
ctdlswDefaultPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswDefaultPortNumber.setStatus('mandatory')
ctdlswPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1), )
if mibBuilder.loadTexts: ctdlswPortTable.setStatus('mandatory')
ctdlswPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswPortName"))
if mibBuilder.loadTexts: ctdlswPortEntry.setStatus('mandatory')
ctdlswPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortIndex.setStatus('mandatory')
ctdlswPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortName.setStatus('mandatory')
ctdlswPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortAddress.setStatus('mandatory')
ctdlswPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswPortAdminStatus.setStatus('mandatory')
ctdlswPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortOperStatus.setStatus('mandatory')
ctdlswPortUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswPortUpTime.setStatus('mandatory')
ctdlswLocalNBFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1), )
if mibBuilder.loadTexts: ctdlswLocalNBFilterTable.setStatus('mandatory')
ctdlswLocalNBFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswLocalNBFilterSrcName"), (0, "CTRON-DLSW-MIB", "ctdlswLocalNBFilterDestName"))
if mibBuilder.loadTexts: ctdlswLocalNBFilterEntry.setStatus('mandatory')
ctdlswLocalNBFilterSrcName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 1), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalNBFilterSrcName.setStatus('mandatory')
ctdlswLocalNBFilterDestName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 2), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalNBFilterDestName.setStatus('mandatory')
ctdlswLocalNBFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswLocalNBFilterControl.setStatus('mandatory')
ctdlswRemoteNBFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2), )
if mibBuilder.loadTexts: ctdlswRemoteNBFilterTable.setStatus('mandatory')
ctdlswRemoteNBFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswRemoteNBFilterSrcName"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteNBFilterDestName"))
if mibBuilder.loadTexts: ctdlswRemoteNBFilterEntry.setStatus('mandatory')
ctdlswRemoteNBFilterSrcName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 1), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteNBFilterSrcName.setStatus('mandatory')
ctdlswRemoteNBFilterDestName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 2), NBName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteNBFilterDestName.setStatus('mandatory')
ctdlswRemoteNBFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswRemoteNBFilterControl.setStatus('mandatory')
ctdlswLocalMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3), )
if mibBuilder.loadTexts: ctdlswLocalMacFilterTable.setStatus('mandatory')
ctdlswLocalMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterSrcAddr"), (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterSrcMask"), (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterDestAddr"), (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterDestMask"))
if mibBuilder.loadTexts: ctdlswLocalMacFilterEntry.setStatus('mandatory')
ctdlswLocalMacFilterSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterSrcAddr.setStatus('mandatory')
ctdlswLocalMacFilterSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterSrcMask.setStatus('mandatory')
ctdlswLocalMacFilterDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterDestAddr.setStatus('mandatory')
ctdlswLocalMacFilterDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswLocalMacFilterDestMask.setStatus('mandatory')
ctdlswLocalMacFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswLocalMacFilterControl.setStatus('mandatory')
ctdlswRemoteMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4), )
if mibBuilder.loadTexts: ctdlswRemoteMacFilterTable.setStatus('mandatory')
ctdlswRemoteMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterSrcAddr"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterSrcMask"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterDestAddr"), (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterDestMask"))
if mibBuilder.loadTexts: ctdlswRemoteMacFilterEntry.setStatus('mandatory')
ctdlswRemoteMacFilterSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterSrcAddr.setStatus('mandatory')
ctdlswRemoteMacFilterSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterSrcMask.setStatus('mandatory')
ctdlswRemoteMacFilterDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterDestAddr.setStatus('mandatory')
ctdlswRemoteMacFilterDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterDestMask.setStatus('mandatory')
ctdlswRemoteMacFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswRemoteMacFilterControl.setStatus('mandatory')
ctdlswTConnTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1), )
if mibBuilder.loadTexts: ctdlswTConnTable.setStatus('mandatory')
ctdlswTConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswTConnRemoteTAddr"))
if mibBuilder.loadTexts: ctdlswTConnEntry.setStatus('mandatory')
ctdlswTConnRemoteTAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnRemoteTAddr.setStatus('mandatory')
ctdlswTConnControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("create", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswTConnControl.setStatus('mandatory')
ctdlswTConnUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnUpTime.setStatus('mandatory')
ctdlswTConnOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pendingDisable", 4), ("pendingEnable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnOperStatus.setStatus('mandatory')
ctdlswTConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configured", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswTConnType.setStatus('mandatory')
ctdlswEventAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventAdminStatus.setStatus('mandatory')
ctdlswEventMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 2), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventMaxEntries.setStatus('mandatory')
ctdlswEventTraceAll = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventTraceAll.setStatus('mandatory')
ctdlswEventFilterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1), )
if mibBuilder.loadTexts: ctdlswEventFilterTable.setStatus('mandatory')
ctdlswEventFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswEventFltrProtocol"), (0, "CTRON-DLSW-MIB", "ctdlswEventFltrIfNum"))
if mibBuilder.loadTexts: ctdlswEventFilterEntry.setStatus('mandatory')
ctdlswEventFltrProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventFltrProtocol.setStatus('mandatory')
ctdlswEventFltrIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventFltrIfNum.setStatus('mandatory')
ctdlswEventFltrControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("delete", 2), ("add", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrControl.setStatus('mandatory')
ctdlswEventFltrType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("misc", 1), ("timer", 2), ("rcv", 4), ("xmit", 8), ("event", 16), ("error", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrType.setStatus('mandatory')
ctdlswEventFltrSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("highest", 1), ("highmed", 2), ("highlow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrSeverity.setStatus('mandatory')
ctdlswEventFltrAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("log", 1), ("trap", 2), ("logTrap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctdlswEventFltrAction.setStatus('mandatory')
ctdlswEventTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1), )
if mibBuilder.loadTexts: ctdlswEventTable.setStatus('mandatory')
ctdlswEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1), ).setIndexNames((0, "CTRON-DLSW-MIB", "ctdlswEventNumber"))
if mibBuilder.loadTexts: ctdlswEventEntry.setStatus('mandatory')
ctdlswEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventNumber.setStatus('mandatory')
ctdlswEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventTime.setStatus('mandatory')
ctdlswEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("misc", 1), ("timer", 2), ("rcv", 4), ("xmit", 8), ("event", 16), ("error", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventType.setStatus('mandatory')
ctdlswEventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("highest", 1), ("highmed", 2), ("highlow", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventSeverity.setStatus('mandatory')
ctdlswEventProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventProtocol.setStatus('mandatory')
ctdlswEventIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventIfNum.setStatus('mandatory')
ctdlswEventTextString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctdlswEventTextString.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DLSW-MIB", ctdlswPortAddress=ctdlswPortAddress, ctdlswEventSeverity=ctdlswEventSeverity, ctdlswEventNumber=ctdlswEventNumber, ctdlswPort=ctdlswPort, ctdlswRemoteMacFilterEntry=ctdlswRemoteMacFilterEntry, ctdlswTConnOperStatus=ctdlswTConnOperStatus, ctdlswEventAdminStatus=ctdlswEventAdminStatus, ctdlswPortAdminStatus=ctdlswPortAdminStatus, ctdlswTConnRemoteTAddr=ctdlswTConnRemoteTAddr, ctdlswDefaultPortNumber=ctdlswDefaultPortNumber, ctdlswRemoteNBFilterSrcName=ctdlswRemoteNBFilterSrcName, ctdlswEventFltrAction=ctdlswEventFltrAction, ctdlswAcceptDynamicTConn=ctdlswAcceptDynamicTConn, ctdlswLocalMacFilterControl=ctdlswLocalMacFilterControl, ctdlswUpTime=ctdlswUpTime, ctdlswEventEntry=ctdlswEventEntry, ctdlswTConnControl=ctdlswTConnControl, ctdlswTConnEntry=ctdlswTConnEntry, ctdlswLocalNBFilterDestName=ctdlswLocalNBFilterDestName, ctdlswTrap=ctdlswTrap, ctdlswEventFltrControl=ctdlswEventFltrControl, ctdlswTConnUpTime=ctdlswTConnUpTime, ctdlswNode=ctdlswNode, ctdlswPortIndex=ctdlswPortIndex, ctdlswLocalMacFilterEntry=ctdlswLocalMacFilterEntry, ctdlswEventLogConfig=ctdlswEventLogConfig, ctdlswPortUpTime=ctdlswPortUpTime, ctdlswRemoteMacFilterSrcAddr=ctdlswRemoteMacFilterSrcAddr, ctdlswLocalNBFilterEntry=ctdlswLocalNBFilterEntry, ctdlswEventFltrIfNum=ctdlswEventFltrIfNum, ctdlswOperStatus=ctdlswOperStatus, ctdlswLocalNBFilterTable=ctdlswLocalNBFilterTable, ctdlswEventTraceAll=ctdlswEventTraceAll, ctdlswTConnType=ctdlswTConnType, ctdlswAdminStatus=ctdlswAdminStatus, ctdlswMacRemoteFilterType=ctdlswMacRemoteFilterType, ctdlswEventProtocol=ctdlswEventProtocol, ctdlswRemoteNBFilterTable=ctdlswRemoteNBFilterTable, ctdlswNBRemoteFilterType=ctdlswNBRemoteFilterType, ctdlswEventTable=ctdlswEventTable, ctdlswFilter=ctdlswFilter, ctdlswLocalMacFilterSrcAddr=ctdlswLocalMacFilterSrcAddr, ctdlswLocalNBFilterControl=ctdlswLocalNBFilterControl, ctdlswEventIfNum=ctdlswEventIfNum, ctdlswRemoteNBFilterDestName=ctdlswRemoteNBFilterDestName, ctdlswMacLocalFilterType=ctdlswMacLocalFilterType, ctdlswPortOperStatus=ctdlswPortOperStatus, ctdlswEventType=ctdlswEventType, NBName=NBName, ctdlswEventFltrSeverity=ctdlswEventFltrSeverity, ctdlswPortName=ctdlswPortName, ctdlswTConnTable=ctdlswTConnTable, ctdlswNodeConfig=ctdlswNodeConfig, ctdlswEventFltrType=ctdlswEventFltrType, ctdlswEventLogTable=ctdlswEventLogTable, ctdlswOperVirtualRingNumber=ctdlswOperVirtualRingNumber, ctdlswPortEntry=ctdlswPortEntry, ctdlswLocalNBFilterSrcName=ctdlswLocalNBFilterSrcName, ctdlswPortTable=ctdlswPortTable, ctdlswEventTextString=ctdlswEventTextString, ctdlswLocalMacFilterTable=ctdlswLocalMacFilterTable, ctdlswRemoteNBFilterEntry=ctdlswRemoteNBFilterEntry, ctdlswNBLocalFilterType=ctdlswNBLocalFilterType, ctdlswEventFilterTable=ctdlswEventFilterTable, ctdlswEventTime=ctdlswEventTime, ctdlswTConn=ctdlswTConn, ctdlswRemoteMacFilterControl=ctdlswRemoteMacFilterControl, ctdlswVersion=ctdlswVersion, ctdlswLocalMacFilterDestAddr=ctdlswLocalMacFilterDestAddr, ctdlswRemoteMacFilterTable=ctdlswRemoteMacFilterTable, ctdlswRemoteNBFilterControl=ctdlswRemoteNBFilterControl, ctdlswLocalMacFilterSrcMask=ctdlswLocalMacFilterSrcMask, ctdlswRemoteMacFilterDestMask=ctdlswRemoteMacFilterDestMask, ctdlswLocalMacFilterDestMask=ctdlswLocalMacFilterDestMask, ctdlswEventFilterEntry=ctdlswEventFilterEntry, ctdlswEventMaxEntries=ctdlswEventMaxEntries, ctdlswEvent=ctdlswEvent, ctdlswEventLogFilterTable=ctdlswEventLogFilterTable, ctdlswRemoteMacFilterSrcMask=ctdlswRemoteMacFilterSrcMask, ctdlswEventFltrProtocol=ctdlswEventFltrProtocol, ctdlswRemoteMacFilterDestAddr=ctdlswRemoteMacFilterDestAddr)
