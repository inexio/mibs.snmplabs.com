#
# PySNMP MIB module CISCO-SECY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SECY-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:11:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
secyIfInterfaceIndex, = mibBuilder.importSymbols("IEEE8021-SECY-MIB", "secyIfInterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Integer32, Unsigned32, IpAddress, Gauge32, ObjectIdentity, ModuleIdentity, Counter32, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Integer32", "Unsigned32", "IpAddress", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibIdentifier", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSecyExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 835))
ciscoSecyExtMIB.setRevisions(('2016-12-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSecyExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSecyExtMIB.setLastUpdated('201612150000Z')
if mibBuilder.loadTexts: ciscoSecyExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSecyExtMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSecyExtMIB.setDescription('A MIB module for extending IEEE8021-SECY-MIB.')
ciscoSecyExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 835, 0))
ciscoSecyExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 835, 1))
ciscoSecyExtMIBStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1))
ciscoSecyExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 835, 2))
cseSecyStatsExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1), )
if mibBuilder.loadTexts: cseSecyStatsExtTable.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsExtTable.setDescription('This table provides the additional statistics information of each SecY supported by the MAC security entity.')
cseSecyStatsExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"))
if mibBuilder.loadTexts: cseSecyStatsExtEntry.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsExtEntry.setDescription('An entry containing counters for statistics or diagnosis for a SecY.')
cseSecyStatsRxTransformErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyStatsRxTransformErrPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsRxTransformErrPkts.setDescription('The number of transform error packets received on this interface.')
cseSecyStatsRxControlPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyStatsRxControlPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsRxControlPkts.setDescription('The number of control packets received on this interface.')
cseSecyStatsRxTaggedCtrlPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyStatsRxTaggedCtrlPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsRxTaggedCtrlPkts.setDescription('The number of tagged control packets received on this interface.')
cseSecyStatsTxTransformErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyStatsTxTransformErrPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsTxTransformErrPkts.setDescription('The number of tranform error packets transmitted via this interface.')
cseSecyStatsTxControlPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyStatsTxControlPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsTxControlPkts.setDescription('The number of control packets transmitted via this interface.')
cseSecyTxSCStatsExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 2), )
if mibBuilder.loadTexts: cseSecyTxSCStatsExtTable.setStatus('current')
if mibBuilder.loadTexts: cseSecyTxSCStatsExtTable.setDescription('A table contains additional statistics information for each transmitting SC in the MAC security entity.')
cseSecyTxSCStatsExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"))
if mibBuilder.loadTexts: cseSecyTxSCStatsExtEntry.setStatus('current')
if mibBuilder.loadTexts: cseSecyTxSCStatsExtEntry.setDescription('An entry containing statistics information of a transmitting SC.')
cseSecyTxSCStatsSANotInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyTxSCStatsSANotInUse.setStatus('current')
if mibBuilder.loadTexts: cseSecyTxSCStatsSANotInUse.setDescription('The number of SA not in use for this transmitting SC.')
cseSecyIfRxStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3), )
if mibBuilder.loadTexts: cseSecyIfRxStatsTable.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxStatsTable.setDescription('A table contains the RX statistics information for each MAC security capable interface.')
cseSecyIfRxStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"))
if mibBuilder.loadTexts: cseSecyIfRxStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxStatsEntry.setDescription('An entry containing the RX statistics information of a MAC Security capable interface.')
cseSecyIfRxUnicastUncontrolledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUnicastUncontrolledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUnicastUncontrolledPkts.setDescription('The number of unicast uncontrolled packets received via this interface.')
cseSecyIfRxMulticastUncontrolledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxMulticastUncontrolledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxMulticastUncontrolledPkts.setDescription('The number of multicast uncontrolled packets received via this interface.')
cseSecyIfRxBroadcastUncontrolledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxBroadcastUncontrolledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxBroadcastUncontrolledPkts.setDescription('The number of broadcast uncontrolled packets received via this interface.')
cseSecyIfRxUncontrolledPktsDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledPktsDrop.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledPktsDrop.setDescription('The number of uncontrolled packets drop received via this interface.')
cseSecyIfRxUncontrolledPktsError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledPktsError.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledPktsError.setDescription('The number of uncontrolled packets error received via this interface.')
cseSecyIfRxUnicastControlledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUnicastControlledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUnicastControlledPkts.setDescription('The number of unicast controlled packets received via this interface.')
cseSecyIfRxMulticastControlledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxMulticastControlledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxMulticastControlledPkts.setDescription('The number of multicast controlled packets received via this interface.')
cseSecyIfRxBroadcastControlledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxBroadcastControlledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxBroadcastControlledPkts.setDescription('The number of broadcast controlled packets received via this interface.')
cseSecyIfRxControlledPktsDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxControlledPktsDrop.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxControlledPktsDrop.setDescription('The number of controlled packets drop received via this interface.')
cseSecyIfRxControlledPktsError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxControlledPktsError.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxControlledPktsError.setDescription('The number of controlled packets error received via this interface.')
cseSecyIfRxUncontrolledOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledOctets.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledOctets.setDescription('The number of uncontrolled octets received via this interface.')
cseSecyIfRxControlledOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxControlledOctets.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxControlledOctets.setDescription('The number of controlled octets received via this interface.')
cseSecyIfRxUncontrolledPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 13), CounterBasedGauge64()).setUnits('Packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledPktRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledPktRate.setDescription('The number of uncontrolled packets per second received via this interface.')
cseSecyIfRxUncontrolledOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 14), CounterBasedGauge64()).setUnits('Bytes per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledOctetRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxUncontrolledOctetRate.setDescription('The number of uncontrolled byte per second received via this interface.')
cseSecyIfRxControlledPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 15), CounterBasedGauge64()).setUnits('Packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxControlledPktRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxControlledPktRate.setDescription('The number of controlled packets per second received via this interface.')
cseSecyIfRxControlledOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 16), CounterBasedGauge64()).setUnits('Bytes per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfRxControlledOctetRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxControlledOctetRate.setDescription('The number of controlled byte per second received via this interface.')
cseSecyIfTxStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4), )
if mibBuilder.loadTexts: cseSecyIfTxStatsTable.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxStatsTable.setDescription('A table contains the TX statistics information for each MAC security capable interface.')
cseSecyIfTxStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"))
if mibBuilder.loadTexts: cseSecyIfTxStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxStatsEntry.setDescription('An entry containing the TX statistics information of a MAC Security capable interface.')
cseSecyIfTxUnicastUncontrolledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUnicastUncontrolledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUnicastUncontrolledPkts.setDescription('The number of unicast uncontrolled packets transmitted via this interface.')
cseSecyIfTxMulticastUncontrolledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxMulticastUncontrolledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxMulticastUncontrolledPkts.setDescription('The number of multicast uncontrolled packets transmitted via this interface.')
cseSecyIfTxBroadcastUncontrolledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxBroadcastUncontrolledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxBroadcastUncontrolledPkts.setDescription('The number of broadcast uncontrolled packets transmitted via this interface.')
cseSecyIfTxUncontrolledPktsDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledPktsDrop.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledPktsDrop.setDescription('The number of uncontrolled packets drop transmitted via this interface.')
cseSecyIfTxUncontrolledPktsError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledPktsError.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledPktsError.setDescription('The number of uncontrolled packets error transmitted via this interface.')
cseSecyIfTxUnicastControlledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUnicastControlledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUnicastControlledPkts.setDescription('The number of unicast controlled packets transmitted via this interface.')
cseSecyIfTxMulticastControlledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxMulticastControlledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxMulticastControlledPkts.setDescription('The number of multicast controlled packets transmitted via this interface.')
cseSecyIfTxBroadcastControlledPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxBroadcastControlledPkts.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxBroadcastControlledPkts.setDescription('The number of broadcast controlled packets transmitted via this interface.')
cseSecyIfTxControlledPktsDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxControlledPktsDrop.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxControlledPktsDrop.setDescription('The number of controlled packets drop transmitted via this interface.')
cseSecyIfTxControlledPktsError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxControlledPktsError.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxControlledPktsError.setDescription('The number of controlled packets error transmitted via this interface.')
cseSecyIfTxUncontrolledOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledOctets.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledOctets.setDescription('The number of uncontrolled octets transmitted via this interface.')
cseSecyIfTxControlledOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxControlledOctets.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxControlledOctets.setDescription('The number of controlled octets transmitted via this interface.')
cseSecyIfTxCommonOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxCommonOctets.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxCommonOctets.setDescription('The number of common octets transmitted via this interface.')
cseSecyIfTxUncontrolledPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 14), CounterBasedGauge64()).setUnits('Packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledPktRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledPktRate.setDescription('The number of uncontrolled packets per second transmitted via this interface.')
cseSecyIfTxUncontrolledOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 15), CounterBasedGauge64()).setUnits('Bytes per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledOctetRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxUncontrolledOctetRate.setDescription('The number of uncontrolled byte per second transmitted via this interface.')
cseSecyIfTxControlledPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 16), CounterBasedGauge64()).setUnits('Packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxControlledPktRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxControlledPktRate.setDescription('The number of controlled packets per second transmitted via this interface.')
cseSecyIfTxControlledOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 17), CounterBasedGauge64()).setUnits('Bytes per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cseSecyIfTxControlledOctetRate.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxControlledOctetRate.setDescription('The number of controlled byte per second transmitted via this interface.')
ciscoSecyExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 1))
ciscoSecyExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2))
cseSecyExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 1, 1)).setObjects(("CISCO-SECY-EXT-MIB", "cseSecyStatsExtGroup"), ("CISCO-SECY-EXT-MIB", "cseSecyTxSCStatsExtGroup"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxStatsGroup"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseSecyExtMIBCompliance = cseSecyExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cseSecyExtMIBCompliance.setDescription('The compliance statement for CISCO-SECY-EXT-MIB. containing default object groups.')
cseSecyStatsExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 1)).setObjects(("CISCO-SECY-EXT-MIB", "cseSecyStatsRxTransformErrPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyStatsRxControlPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyStatsRxTaggedCtrlPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyStatsTxTransformErrPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyStatsTxControlPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseSecyStatsExtGroup = cseSecyStatsExtGroup.setStatus('current')
if mibBuilder.loadTexts: cseSecyStatsExtGroup.setDescription('A collection of objects providing additional SecY statistics information.')
cseSecyTxSCStatsExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 2)).setObjects(("CISCO-SECY-EXT-MIB", "cseSecyTxSCStatsSANotInUse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseSecyTxSCStatsExtGroup = cseSecyTxSCStatsExtGroup.setStatus('current')
if mibBuilder.loadTexts: cseSecyTxSCStatsExtGroup.setDescription('A collection of objects providing the addtional transmitting SC Statistics information.')
cseSecyIfRxStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 3)).setObjects(("CISCO-SECY-EXT-MIB", "cseSecyIfRxUnicastUncontrolledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxMulticastUncontrolledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxBroadcastUncontrolledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledPktsDrop"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledPktsError"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUnicastControlledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxMulticastControlledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxBroadcastControlledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledPktsDrop"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledPktsError"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledOctets"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledOctets"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledPktRate"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledOctetRate"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledPktRate"), ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledOctetRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseSecyIfRxStatsGroup = cseSecyIfRxStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfRxStatsGroup.setDescription('A collection of objects providing the Rx statistics for the MAC security capable interface.')
cseSecyIfTxStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 4)).setObjects(("CISCO-SECY-EXT-MIB", "cseSecyIfTxUnicastUncontrolledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxMulticastUncontrolledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxBroadcastUncontrolledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledPktsDrop"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledPktsError"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUnicastControlledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxMulticastControlledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxBroadcastControlledPkts"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledPktsDrop"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledPktsError"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledOctets"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledOctets"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxCommonOctets"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledPktRate"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledOctetRate"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledPktRate"), ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledOctetRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseSecyIfTxStatsGroup = cseSecyIfTxStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cseSecyIfTxStatsGroup.setDescription('A collection of objects providing the Tx statistics for the MAC security capable interface.')
mibBuilder.exportSymbols("CISCO-SECY-EXT-MIB", cseSecyTxSCStatsExtTable=cseSecyTxSCStatsExtTable, cseSecyStatsTxControlPkts=cseSecyStatsTxControlPkts, cseSecyIfRxBroadcastControlledPkts=cseSecyIfRxBroadcastControlledPkts, cseSecyIfRxUncontrolledPktRate=cseSecyIfRxUncontrolledPktRate, cseSecyIfRxUncontrolledPktsError=cseSecyIfRxUncontrolledPktsError, cseSecyIfTxControlledOctets=cseSecyIfTxControlledOctets, cseSecyTxSCStatsExtGroup=cseSecyTxSCStatsExtGroup, cseSecyIfTxStatsGroup=cseSecyIfTxStatsGroup, cseSecyIfTxBroadcastControlledPkts=cseSecyIfTxBroadcastControlledPkts, cseSecyTxSCStatsSANotInUse=cseSecyTxSCStatsSANotInUse, cseSecyIfTxControlledPktsError=cseSecyIfTxControlledPktsError, cseSecyStatsRxTaggedCtrlPkts=cseSecyStatsRxTaggedCtrlPkts, cseSecyIfRxMulticastUncontrolledPkts=cseSecyIfRxMulticastUncontrolledPkts, cseSecyIfRxMulticastControlledPkts=cseSecyIfRxMulticastControlledPkts, cseSecyIfRxControlledPktsDrop=cseSecyIfRxControlledPktsDrop, cseSecyIfTxUnicastControlledPkts=cseSecyIfTxUnicastControlledPkts, cseSecyIfTxMulticastControlledPkts=cseSecyIfTxMulticastControlledPkts, cseSecyIfRxControlledPktRate=cseSecyIfRxControlledPktRate, cseSecyIfTxStatsTable=cseSecyIfTxStatsTable, cseSecyTxSCStatsExtEntry=cseSecyTxSCStatsExtEntry, cseSecyStatsTxTransformErrPkts=cseSecyStatsTxTransformErrPkts, cseSecyStatsExtTable=cseSecyStatsExtTable, cseSecyIfRxStatsEntry=cseSecyIfRxStatsEntry, cseSecyIfRxStatsGroup=cseSecyIfRxStatsGroup, cseSecyIfRxUncontrolledOctets=cseSecyIfRxUncontrolledOctets, cseSecyIfTxControlledPktsDrop=cseSecyIfTxControlledPktsDrop, ciscoSecyExtMIBGroups=ciscoSecyExtMIBGroups, cseSecyIfRxControlledOctets=cseSecyIfRxControlledOctets, cseSecyStatsRxControlPkts=cseSecyStatsRxControlPkts, cseSecyIfRxControlledPktsError=cseSecyIfRxControlledPktsError, cseSecyIfRxUnicastControlledPkts=cseSecyIfRxUnicastControlledPkts, cseSecyIfTxBroadcastUncontrolledPkts=cseSecyIfTxBroadcastUncontrolledPkts, cseSecyIfRxUnicastUncontrolledPkts=cseSecyIfRxUnicastUncontrolledPkts, cseSecyIfTxUncontrolledPktsDrop=cseSecyIfTxUncontrolledPktsDrop, cseSecyIfTxCommonOctets=cseSecyIfTxCommonOctets, ciscoSecyExtMIBNotifs=ciscoSecyExtMIBNotifs, cseSecyIfRxControlledOctetRate=cseSecyIfRxControlledOctetRate, cseSecyStatsExtEntry=cseSecyStatsExtEntry, ciscoSecyExtMIBStatsObjects=ciscoSecyExtMIBStatsObjects, cseSecyIfRxStatsTable=cseSecyIfRxStatsTable, cseSecyStatsRxTransformErrPkts=cseSecyStatsRxTransformErrPkts, PYSNMP_MODULE_ID=ciscoSecyExtMIB, ciscoSecyExtMIBConform=ciscoSecyExtMIBConform, ciscoSecyExtMIBCompliances=ciscoSecyExtMIBCompliances, cseSecyIfTxMulticastUncontrolledPkts=cseSecyIfTxMulticastUncontrolledPkts, cseSecyIfTxUncontrolledOctetRate=cseSecyIfTxUncontrolledOctetRate, cseSecyExtMIBCompliance=cseSecyExtMIBCompliance, cseSecyIfRxBroadcastUncontrolledPkts=cseSecyIfRxBroadcastUncontrolledPkts, cseSecyIfRxUncontrolledPktsDrop=cseSecyIfRxUncontrolledPktsDrop, cseSecyIfTxControlledPktRate=cseSecyIfTxControlledPktRate, cseSecyIfTxUnicastUncontrolledPkts=cseSecyIfTxUnicastUncontrolledPkts, cseSecyIfTxControlledOctetRate=cseSecyIfTxControlledOctetRate, ciscoSecyExtMIBObjects=ciscoSecyExtMIBObjects, cseSecyIfRxUncontrolledOctetRate=cseSecyIfRxUncontrolledOctetRate, cseSecyStatsExtGroup=cseSecyStatsExtGroup, cseSecyIfTxUncontrolledPktsError=cseSecyIfTxUncontrolledPktsError, ciscoSecyExtMIB=ciscoSecyExtMIB, cseSecyIfTxUncontrolledPktRate=cseSecyIfTxUncontrolledPktRate, cseSecyIfTxUncontrolledOctets=cseSecyIfTxUncontrolledOctets, cseSecyIfTxStatsEntry=cseSecyIfTxStatsEntry)
