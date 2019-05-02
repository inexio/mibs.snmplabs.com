#
# PySNMP MIB module INTEL-IGMP-PRUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-IGMP-PRUNING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, Bits, NotificationType, Counter64, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Bits", "NotificationType", "Counter64", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
igmppru = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 35))
conf = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 35, 1))
confIgmpPruEnabled = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIgmpPruEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruEnabled.setDescription('The administrative status requested by management for IGMP pruning. The value enabled(1) indicates that IGMP pruning should be enabled on this device, in all VLANs, on all ports for which it has not been specifically disabled. When disabled(2), IGMP pruning is disabled, in all VLANs, on all ports.')
confIgmpPruTimer = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIgmpPruTimer.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruTimer.setDescription('IGMP pruning timer value in seconds. The timer value should be greater than two times the interval between IGMP general queries.')
confIgmpPruPortTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3), )
if mibBuilder.loadTexts: confIgmpPruPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruPortTable.setDescription('Port configuration table')
confIgmpPruPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3, 1), ).setIndexNames((0, "INTEL-IGMP-PRUNING-MIB", "confIgmpPruPortIndex"))
if mibBuilder.loadTexts: confIgmpPruPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruPortEntry.setDescription('An entry containing the objects for configuration and status of a port.')
confIgmpPruPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: confIgmpPruPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruPortIndex.setDescription('An index value that uniquely identifies an interface. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
confIgmpPruPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIgmpPruPortEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruPortEnabled.setDescription('The state of IGMP pruning operation on this port. The value enabled(1) indicates that IGMP pruning is enabled on this port, in all VLANs, as long as confIgmpPruEnabled is also enabled for this device. When disabled(2) but confIgmpPruEnabled is still enabled for the device, IGMP pruning is disabled on this port in all VLANs.')
confIgmpPruAllowAsQuerier = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confIgmpPruAllowAsQuerier.setStatus('mandatory')
if mibBuilder.loadTexts: confIgmpPruAllowAsQuerier.setDescription('The administrative status requested by management for allowing this device to participate in the IGMP querier/non-querier election. The value enabled(1) indicates that the device will participate in the IGMP querier/non-querier election scheme and thus may transmit IGMP queries, in all VLANs, on all ports for which IGMP pruning is also enabled. When disabled(2), the device will NOT participate in the IGMP querier/non-querier election scheme and will NOT transmit any IGMP queries, in all VLANs, on all ports. ')
mibBuilder.exportSymbols("INTEL-IGMP-PRUNING-MIB", confIgmpPruPortEnabled=confIgmpPruPortEnabled, igmppru=igmppru, confIgmpPruPortEntry=confIgmpPruPortEntry, confIgmpPruPortIndex=confIgmpPruPortIndex, confIgmpPruAllowAsQuerier=confIgmpPruAllowAsQuerier, conf=conf, confIgmpPruPortTable=confIgmpPruPortTable, confIgmpPruEnabled=confIgmpPruEnabled, confIgmpPruTimer=confIgmpPruTimer)