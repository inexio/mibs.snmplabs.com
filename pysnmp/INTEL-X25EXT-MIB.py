#
# PySNMP MIB module INTEL-X25EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-X25EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, Counter32, ModuleIdentity, NotificationType, Gauge32, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "Counter32", "ModuleIdentity", "NotificationType", "Gauge32", "iso", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

x25ext = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 27))
x25extCircuit = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 27, 1))
x25extCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1), )
if mibBuilder.loadTexts: x25extCircuitTable.setStatus('mandatory')
x25extCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1), ).setIndexNames((0, "INTEL-X25EXT-MIB", "x25extCircuitIndex"), (0, "INTEL-X25EXT-MIB", "x25extCircuitChannel"))
if mibBuilder.loadTexts: x25extCircuitEntry.setStatus('mandatory')
x25extCircuitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitIndex.setStatus('mandatory')
x25extCircuitChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitChannel.setStatus('mandatory')
x25extCircuitLogicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 3), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitLogicalIndex.setStatus('mandatory')
x25extCircuitPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitPacketSize.setStatus('mandatory')
x25extCircuitWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitWindowSize.setStatus('mandatory')
x25extCircuitTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitTimeout.setStatus('mandatory')
x25extCircuitOutResets = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitOutResets.setStatus('mandatory')
x25extCircuitOutFlowStuckResets = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 27, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25extCircuitOutFlowStuckResets.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-X25EXT-MIB", x25extCircuitEntry=x25extCircuitEntry, x25extCircuitChannel=x25extCircuitChannel, x25extCircuitPacketSize=x25extCircuitPacketSize, x25extCircuitWindowSize=x25extCircuitWindowSize, x25extCircuitLogicalIndex=x25extCircuitLogicalIndex, x25ext=x25ext, IfIndexType=IfIndexType, x25extCircuitOutFlowStuckResets=x25extCircuitOutFlowStuckResets, x25extCircuitTimeout=x25extCircuitTimeout, x25extCircuitIndex=x25extCircuitIndex, x25extCircuitOutResets=x25extCircuitOutResets, x25extCircuitTable=x25extCircuitTable, x25extCircuit=x25extCircuit)
