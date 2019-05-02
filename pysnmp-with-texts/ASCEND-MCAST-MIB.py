#
# PySNMP MIB module ASCEND-MCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MCAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
mCastGroup, = mibBuilder.importSymbols("ASCEND-MIB", "mCastGroup")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, NotificationType, TimeTicks, IpAddress, Gauge32, Bits, Integer32, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "NotificationType", "TimeTicks", "IpAddress", "Gauge32", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
heartBeatMulticastGroupAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatMulticastGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: heartBeatMulticastGroupAddress.setDescription('Multicast Group address used to receive HeartBeat packets.')
heartBeatSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatSourceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: heartBeatSourceAddress.setDescription('Source address of last valid heartbeat packet received.')
heartBeatSlotTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatSlotTimeInterval.setStatus('mandatory')
if mibBuilder.loadTexts: heartBeatSlotTimeInterval.setDescription('Number of seconds MAX waits to receive a valid heartBeat packet.')
heartBeatSlotCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatSlotCount.setStatus('mandatory')
if mibBuilder.loadTexts: heartBeatSlotCount.setDescription('Number of slot intervals MAX waits before checking if expected number of heartbeat packets received or not.')
heartBeatPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatPacketCount.setStatus('mandatory')
if mibBuilder.loadTexts: heartBeatPacketCount.setDescription('Number of heartbeat packets received in Slot Count intervals when entering Alarm Mode.')
mibBuilder.exportSymbols("ASCEND-MCAST-MIB", heartBeatPacketCount=heartBeatPacketCount, heartBeatSlotCount=heartBeatSlotCount, heartBeatMulticastGroupAddress=heartBeatMulticastGroupAddress, heartBeatSlotTimeInterval=heartBeatSlotTimeInterval, heartBeatSourceAddress=heartBeatSourceAddress)