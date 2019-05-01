#
# PySNMP MIB module PVC-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PVC-SERVICE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:42:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
frCircuitDlci, frCircuitIfIndex = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "frCircuitDlci", "frCircuitIfIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ObjectIdentity, iso, Bits, ModuleIdentity, Unsigned32, IpAddress, Counter64, MibIdentifier, Counter32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "Bits", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter64", "MibIdentifier", "Counter32", "NotificationType", "Integer32")
TextualConvention, TruthValue, PhysAddress, MacAddress, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "PhysAddress", "MacAddress", "RowStatus", "DisplayString")
pgService = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 6))
if mibBuilder.loadTexts: pgService.setLastUpdated('9803030000Z')
if mibBuilder.loadTexts: pgService.setOrganization('PairGain Technology')
if mibBuilder.loadTexts: pgService.setContactInfo('')
if mibBuilder.loadTexts: pgService.setDescription('The module defines the MIB for PVC Service configuration.')
pgServiceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1))
class PgPvcServiceType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("ipoa", 2), ("lant", 3), ("ppp", 4), ("frame-relay", 5), ("null", 6), ("ramp1483", 7))

class PgXdslFrameType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("mac", 2))

pgXdslServiceTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1), )
if mibBuilder.loadTexts: pgXdslServiceTable.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceTable.setDescription('A table of xDSL port entries that defines the Service Application and other port/interface related parameters needed to use the xDSL port for that service.')
pgXdslServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgXdslServiceEntry.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceEntry.setDescription('An entry in the pgXdslServiceTable.')
pgXdslServiceSubscriberName = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceSubscriberName.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceSubscriberName.setDescription('The Subscriber name.')
pgXdslServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 2), PgPvcServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceType.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceType.setDescription('The Service name as defined by PgPvcServiceType.')
pgXdslServiceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceMacAddress.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceMacAddress.setDescription('The Physical(MAC) address of the xDSL port.')
pgXdslServiceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceIpAddress.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceIpAddress.setDescription('The IP address of the xDSL port.')
pgXdslServiceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceSubnetMask.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceSubnetMask.setDescription('The Subnet mask for the Interface.')
pgXdslServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgXdslServiceRowStatus.setStatus('current')
if mibBuilder.loadTexts: pgXdslServiceRowStatus.setDescription('This object allows entries to be created and deleted in this table. The RowStatus should be out of the ACTIVE state for other columns to be modified.')
class PgPvcServiceEncapType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("vc-mux-iso", 2), ("vc-mux-ip", 3), ("vc-mux-8023", 4), ("llc-iso", 5), ("llc-ip", 6), ("llc-8023-crc", 7), ("llc-8023", 8), ("vc-mux-ppp", 9), ("llc-ppp", 10), ("vc-mux-ramp1483", 11))

pgPvcServiceTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2), )
if mibBuilder.loadTexts: pgPvcServiceTable.setStatus('current')
if mibBuilder.loadTexts: pgPvcServiceTable.setDescription('A table of PVC entries (as described by pgPvcServiceSarIfIndex and pgPvcServiceSarIfIndex/Vpi/Vci ) that defines the Service Application name such as LANT/PPP etc., and maps the PVC to the xDSL port.')
pgPvcServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1), ).setIndexNames((0, "PVC-SERVICE-MIB", "pgPvcServiceSarVpi"), (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVci"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgPvcServiceEntry.setStatus('current')
if mibBuilder.loadTexts: pgPvcServiceEntry.setDescription('The Route information that maps Network numbers to the ifIndex of the xDSL port.')
pgPvcServiceSarVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceSarVpi.setStatus('current')
if mibBuilder.loadTexts: pgPvcServiceSarVpi.setDescription('The SAR VPI.')
pgPvcServiceSarVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceSarVci.setStatus('current')
if mibBuilder.loadTexts: pgPvcServiceSarVci.setDescription('The SAR VCI.')
pgPvcServiceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceIpAddress.setStatus('deprecated')
if mibBuilder.loadTexts: pgPvcServiceIpAddress.setDescription('The IP address.')
pgPvcServiceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceSubnetMask.setStatus('deprecated')
if mibBuilder.loadTexts: pgPvcServiceSubnetMask.setDescription('The Subnet mask for the Interface.')
pgPvcServiceEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 5), PgPvcServiceEncapType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceEncapType.setStatus('deprecated')
if mibBuilder.loadTexts: pgPvcServiceEncapType.setDescription('The encapsulation mode used by the PVC.')
pgPvcServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgPvcServiceRowStatus.setStatus('current')
if mibBuilder.loadTexts: pgPvcServiceRowStatus.setDescription('This object allows entries to be created and deleted in this table. The RowStatus should be out of the ACTIVE state for other columns to be modified.')
pgNextSarVciTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3), )
if mibBuilder.loadTexts: pgNextSarVciTable.setStatus('current')
if mibBuilder.loadTexts: pgNextSarVciTable.setDescription('This object is referenced by the slot since each SDSL card has a certain number of VCI entries. The value returned can be used for the next VCI value.')
pgNextSarVciEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgNextSarVciEntry.setStatus('current')
if mibBuilder.loadTexts: pgNextSarVciEntry.setDescription('The slot dependent table that gives the next available VCI for a particular card.')
pgNextSarSlotVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgNextSarSlotVci.setStatus('current')
if mibBuilder.loadTexts: pgNextSarSlotVci.setDescription('contains an appropriate value to be used for pgPvcServiceSarVci when creating entries in the pgPvcServiceTable. The value 0 indicates that no unassigned entries are available. To obtain the pgPvcServiceSarVci value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object. This value is updated whenever a VCL is set up.')
pgPvcFrServiceTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4), )
if mibBuilder.loadTexts: pgPvcFrServiceTable.setStatus('current')
if mibBuilder.loadTexts: pgPvcFrServiceTable.setDescription('A table of PVC entries (as described by pgPvcServiceSarIfIndex and pgPvcServiceSarIfIndex/Vpi/Vci ) that defines the Service Application as other, and maps the PVC to the xDSL port.')
pgPvcFrServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1), ).setIndexNames((0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"), (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"), (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVpi"), (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVci"))
if mibBuilder.loadTexts: pgPvcFrServiceEntry.setStatus('current')
if mibBuilder.loadTexts: pgPvcFrServiceEntry.setDescription('The Route information that maps Network numbers to the ifIndex of xDSL port.')
pgPvcFrServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgPvcFrServiceRowStatus.setStatus('current')
if mibBuilder.loadTexts: pgPvcFrServiceRowStatus.setDescription('This object allows entries to be created and deleted in this table. The RowStatus should be out of the ACTIVE state for other columns to be modified.')
pgPvcFrSubSystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 8))).clone(namedValues=NamedValues(("frf5", 5), ("frf8", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgPvcFrSubSystemType.setStatus('current')
if mibBuilder.loadTexts: pgPvcFrSubSystemType.setDescription('This object allows entries to be created and deleted in this table. The RowStatus should be out of the ACTIVE state for other columns to be modified.')
mibBuilder.exportSymbols("PVC-SERVICE-MIB", pgPvcServiceSarVci=pgPvcServiceSarVci, pgXdslServiceSubnetMask=pgXdslServiceSubnetMask, pgPvcServiceTable=pgPvcServiceTable, PgPvcServiceType=PgPvcServiceType, PgPvcServiceEncapType=PgPvcServiceEncapType, pgPvcFrServiceRowStatus=pgPvcFrServiceRowStatus, pgPvcServiceSubnetMask=pgPvcServiceSubnetMask, pgNextSarVciTable=pgNextSarVciTable, pgXdslServiceTable=pgXdslServiceTable, pgXdslServiceType=pgXdslServiceType, pgXdslServiceEntry=pgXdslServiceEntry, pgXdslServiceSubscriberName=pgXdslServiceSubscriberName, pgPvcFrServiceTable=pgPvcFrServiceTable, pgPvcFrSubSystemType=pgPvcFrSubSystemType, pgPvcServiceEntry=pgPvcServiceEntry, pgServiceObjects=pgServiceObjects, pgXdslServiceIpAddress=pgXdslServiceIpAddress, pgNextSarVciEntry=pgNextSarVciEntry, pgPvcServiceIpAddress=pgPvcServiceIpAddress, pgXdslServiceMacAddress=pgXdslServiceMacAddress, pgService=pgService, pgPvcFrServiceEntry=pgPvcFrServiceEntry, pgPvcServiceSarVpi=pgPvcServiceSarVpi, pgXdslServiceRowStatus=pgXdslServiceRowStatus, PgXdslFrameType=PgXdslFrameType, pgPvcServiceRowStatus=pgPvcServiceRowStatus, pgNextSarSlotVci=pgNextSarSlotVci, PYSNMP_MODULE_ID=pgService, pgPvcServiceEncapType=pgPvcServiceEncapType)
