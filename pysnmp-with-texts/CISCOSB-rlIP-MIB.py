#
# PySNMP MIB module CISCOSB-rlIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-rlIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressPrefixLength, InetAddressType, InetAddress, InetZoneIndex, InetVersion = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetAddress", "InetZoneIndex", "InetVersion")
IpAddressStatusTC, IpAddressOriginTC = mibBuilder.importSymbols("IP-MIB", "IpAddressStatusTC", "IpAddressOriginTC")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Counter32, IpAddress, mib_2, MibIdentifier, Counter64, Unsigned32, zeroDotZero, TimeTicks, ModuleIdentity, ObjectIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "IpAddress", "mib-2", "MibIdentifier", "Counter64", "Unsigned32", "zeroDotZero", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32")
TestAndIncr, TimeStamp, DisplayString, RowStatus, RowPointer, PhysAddress, TruthValue, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "TimeStamp", "DisplayString", "RowStatus", "RowPointer", "PhysAddress", "TruthValue", "TextualConvention", "StorageType")
rlIp = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250))
rlIp.setRevisions(('2013-06-16 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlIp.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlIp.setLastUpdated('201306161200Z')
if mibBuilder.loadTexts: rlIp.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlIp.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlIp.setDescription('The private MIB module definition for Auto Configured IPv6 Address representation.')
class RlIpAddressOriginTC(TextualConvention, Integer32):
    description = 'The origin of the address. following are same as ipAddressOriginTC in standard MIB: manual(2) indicates that the address was manually configured to a specified address, e.g., by user configuration. dhcp(4) indicates an address that was assigned to this system by a DHCP server. linklayer(5) indicates an address created by IPv6 stateless auto-configuration. random(6) indicates an address chosen by the system at random, e.g., an IPv4 address within 169.254/16, or an RFC 3041 privacy address. following are additional to standard MIB: autoConfig(7) indicates that the address was auto configured configured to a specified address, e.g., not by user configuration. eui64(8) indicates that the address was partially configured configured to a specified address, e.g., address suffix is based on MAC address with EUI-64 representation. tunnelIsatap(9) indicates that the address an ISATATP tunnel representation. tunnelIsatap(10) indicates that the address an 6to4 tunnel representation. tunnelIsatap(11) indicates that the address was partially configured configured to a specified address, e.g., address prefix is preconfigured. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("manual", 2), ("dhcp", 4), ("linklayer", 5), ("random", 6), ("autoConfig", 7), ("eui64", 8), ("tunnelIsatap", 9), ("tunnel6to4", 10), ("generalPrefix", 11))

rlIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1), )
if mibBuilder.loadTexts: rlIpAddressTable.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressTable.setDescription("This table contains addressing information relevant to the entity's interfaces. in addition to ipAddressTable defined in standard MIB a represenattion of IPv6 addresses based on additionl address origin such as EUI-64, general prefix etc. In this case the address information is partial address information. Together with the address origin and the general prefix (when needed) user can construct full address information. The index (key) for this table includes this information additionally to the address.")
rlIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1), ).setIndexNames((0, "CISCOSB-rlIP-MIB", "rlIpAddressAddrType"), (0, "CISCOSB-rlIP-MIB", "rlIpAddressAddr"), (0, "CISCOSB-rlIP-MIB", "rlIpAddressOrigin"), (0, "CISCOSB-rlIP-MIB", "rlIpAddressGeneralPrefixName"))
if mibBuilder.loadTexts: rlIpAddressEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressEntry.setDescription('An address mapping for a particular interface.')
rlIpAddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlIpAddressAddrType.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressAddrType.setDescription('The address type of rlIpAddressAddr.')
rlIpAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: rlIpAddressAddr.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressAddr.setDescription("The IP address to which this entry's addressing information pertains. The address type of this object is specified in rlIpAddressAddrType. In case of auto-configure address such as eui-64, general-prefix and others it contains the partial address before appropriate manipulation. Implementors need to be aware that if the size of rlIpAddressAddr exceeds 116 octets, then OIDS of instances of columns in this row will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
rlIpAddressOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 3), RlIpAddressOriginTC())
if mibBuilder.loadTexts: rlIpAddressOrigin.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressOrigin.setDescription('The origin of the address.')
rlIpAddressGeneralPrefixName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 4), DisplayString())
if mibBuilder.loadTexts: rlIpAddressGeneralPrefixName.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressGeneralPrefixName.setDescription('The name assigned to the prefix.')
rlIpAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlIpAddressIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
rlIpAddressExtdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unicast", 1), ("anycast", 2), ("broadcast", 3), ("multicast", 4))).clone('unicast')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlIpAddressExtdType.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressExtdType.setDescription('Extend standard field ipAddressType to multicast')
rlIpAddressPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 7), RowPointer().clone((0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpAddressPrefix.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressPrefix.setDescription('A pointer to the row in the prefix table to which this address belongs. May be { 0 0 } if there is no such row.')
rlIpAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 8), IpAddressStatusTC().clone('preferred')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlIpAddressStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressStatus.setDescription('The status of the address, describing if the address can be used for communication. In the absence of other information, an IPv4 address is always preferred(1).')
rlIpAddressCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpAddressCreated.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressCreated.setDescription('The value of sysUpTime at the time this entry was created. If this entry was created prior to the last re- initialization of the local network management subsystem, then this object contains a zero value.')
rlIpAddressLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpAddressLastChanged.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressLastChanged.setDescription('The value of sysUpTime at the time this entry was last updated. If this entry was updated prior to the last re- initialization of the local network management subsystem, then this object contains a zero value.')
rlIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlIpAddressRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressRowStatus.setDescription('The status of this conceptual row. The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified. The value of this object has no effect on whether other objects in this conceptual row can be modified. A conceptual row can not be made active until the rlIpAddressIfIndex has been set to a valid index.')
rlIpAddressStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 12), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlIpAddressStorageType.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressStorageType.setDescription("The storage type for this conceptual row. If this object has a value of 'permanent', then no other objects are required to be able to be modified.")
rlIpAddressExtdPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 13), InetAddressPrefixLength().clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlIpAddressExtdPrefixLength.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressExtdPrefixLength.setDescription('The prefix length of this address.')
rlIpAddressCompleteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 250, 1, 1, 14), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpAddressCompleteAddr.setStatus('current')
if mibBuilder.loadTexts: rlIpAddressCompleteAddr.setDescription("The Complete IP address to which this entry's addressing information pertains. In case of auto-configure address such as eui-64, general-prefix and others it contains the complete address after appropriate manipulation")
mibBuilder.exportSymbols("CISCOSB-rlIP-MIB", rlIpAddressAddr=rlIpAddressAddr, rlIpAddressTable=rlIpAddressTable, RlIpAddressOriginTC=RlIpAddressOriginTC, rlIpAddressEntry=rlIpAddressEntry, rlIpAddressOrigin=rlIpAddressOrigin, rlIpAddressCompleteAddr=rlIpAddressCompleteAddr, rlIpAddressCreated=rlIpAddressCreated, rlIpAddressExtdType=rlIpAddressExtdType, PYSNMP_MODULE_ID=rlIp, rlIpAddressAddrType=rlIpAddressAddrType, rlIpAddressPrefix=rlIpAddressPrefix, rlIpAddressRowStatus=rlIpAddressRowStatus, rlIpAddressIfIndex=rlIpAddressIfIndex, rlIpAddressExtdPrefixLength=rlIpAddressExtdPrefixLength, rlIpAddressStatus=rlIpAddressStatus, rlIp=rlIp, rlIpAddressStorageType=rlIpAddressStorageType, rlIpAddressGeneralPrefixName=rlIpAddressGeneralPrefixName, rlIpAddressLastChanged=rlIpAddressLastChanged)
