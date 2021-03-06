#
# PySNMP MIB module RADLAN-rlDvmrp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-rlDvmrp-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:50:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dvmrpRouteNextHopIfIndex, dvmrpRouteNextHopSource, dvmrpRouteNextHopSourceMask, dvmrpRouteNextHopEntry = mibBuilder.importSymbols("DVMRP-STD-MIB", "dvmrpRouteNextHopIfIndex", "dvmrpRouteNextHopSource", "dvmrpRouteNextHopSourceMask", "dvmrpRouteNextHopEntry")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
rnd, rndNotifications = mibBuilder.importSymbols("RADLAN-MIB", "rnd", "rndNotifications")
rlIPmulticast, = mibBuilder.importSymbols("RADLAN-rlIPMulticast-MIB", "rlIPmulticast")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, TimeTicks, MibIdentifier, Counter64, Gauge32, Unsigned32, Integer32, Bits, ObjectIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64", "Gauge32", "Unsigned32", "Integer32", "Bits", "ObjectIdentity", "Counter32", "iso")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
rlDvmrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 46, 4))
rlDvmrp.setRevisions(('2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDvmrp.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlDvmrp.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: rlDvmrp.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlDvmrp.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlDvmrp.setDescription('The private MIB module definition for IP Multicast DVMRP support in Radlan devices.')
rlDvmrpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDvmrpMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpMibVersion.setDescription("MIB's version, the current version is 1.")
rlDvmrpEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpEnable.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpEnable.setDescription('The enabled status of Dvmrp on this router.')
rlDvmrpProbeInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 4), Integer32().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpProbeInterval.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpProbeInterval.setDescription('The default interval at which periodic DVMRP Probe messages are to be sent.')
rlDvmrpNeighborTimeOutInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(25, 400)).clone(35)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpNeighborTimeOutInterval.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpNeighborTimeOutInterval.setDescription('The default interval, if expired the Neighbor need to be deleted from Interface.')
rlDvmrpMinFlashUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 6), Integer32().clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpMinFlashUpdateInterval.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpMinFlashUpdateInterval.setDescription('The min interval at which the DVMRP Fash (Report msg) messages are to be sent.')
rlDvmrpRouteReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 7), Integer32().clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpRouteReportInterval.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpRouteReportInterval.setDescription('The default interval at which periodic DVMRP Report messages are to be sent.')
rlDvmrpRouteExpirationTime = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 8), Integer32().clone(140)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpRouteExpirationTime.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpRouteExpirationTime.setDescription('The default interval at which route expired.')
rlDvmrpPruneLifetime = MibScalar((1, 3, 6, 1, 4, 1, 89, 46, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 7200)).clone(200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDvmrpPruneLifetime.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpPruneLifetime.setDescription('The default value of prune interval to be send upstream.')
rlDvmrpRouteDesignatedForwarderExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 46, 4, 10), )
if mibBuilder.loadTexts: rlDvmrpRouteDesignatedForwarderExtTable.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpRouteDesignatedForwarderExtTable.setDescription('The (conceptual) table listing the designated forwarder for each source mask and interface.')
rlDvmrpRouteDesignatedForwarderExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 46, 4, 10, 1), )
dvmrpRouteNextHopEntry.registerAugmentions(("RADLAN-rlDvmrp-MIB", "rlDvmrpRouteDesignatedForwarderExtEntry"))
rlDvmrpRouteDesignatedForwarderExtEntry.setIndexNames(*dvmrpRouteNextHopEntry.getIndexNames())
if mibBuilder.loadTexts: rlDvmrpRouteDesignatedForwarderExtEntry.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpRouteDesignatedForwarderExtEntry.setDescription('An entry (conceptual row) in the rlDvmrpRouteDesignatedForwarderExtTable. Specifies the designated forwarder for this source mask and interface.')
rlDvmrpRouteDesignatedForwarder = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 46, 4, 10, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDvmrpRouteDesignatedForwarder.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpRouteDesignatedForwarder.setDescription('The address of the designated forwarder for the specific Source Mask and Interface.')
rlDvmrpTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 155)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlDvmrpTableOverflow.setStatus('current')
if mibBuilder.loadTexts: rlDvmrpTableOverflow.setDescription('A DVMRP Table overflows.')
mibBuilder.exportSymbols("RADLAN-rlDvmrp-MIB", rlDvmrpMinFlashUpdateInterval=rlDvmrpMinFlashUpdateInterval, rlDvmrpEnable=rlDvmrpEnable, rlDvmrpRouteDesignatedForwarder=rlDvmrpRouteDesignatedForwarder, rlDvmrpMibVersion=rlDvmrpMibVersion, rlDvmrpProbeInterval=rlDvmrpProbeInterval, rlDvmrpPruneLifetime=rlDvmrpPruneLifetime, rlDvmrpRouteDesignatedForwarderExtTable=rlDvmrpRouteDesignatedForwarderExtTable, rlDvmrpTableOverflow=rlDvmrpTableOverflow, rlDvmrpRouteExpirationTime=rlDvmrpRouteExpirationTime, rlDvmrpRouteDesignatedForwarderExtEntry=rlDvmrpRouteDesignatedForwarderExtEntry, rlDvmrpNeighborTimeOutInterval=rlDvmrpNeighborTimeOutInterval, PYSNMP_MODULE_ID=rlDvmrp, rlDvmrpRouteReportInterval=rlDvmrpRouteReportInterval, rlDvmrp=rlDvmrp)
