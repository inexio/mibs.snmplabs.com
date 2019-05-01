#
# PySNMP MIB module A3COM-HUAWEI-QOS-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-QOS-CAPABILITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cSNMPAgCpb, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cSNMPAgCpb")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, NotificationType, Unsigned32, IpAddress, MibIdentifier, Gauge32, iso, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Gauge32", "iso", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1))
if mibBuilder.loadTexts: h3cQosCapability.setLastUpdated('200508300000Z')
if mibBuilder.loadTexts: h3cQosCapability.setOrganization('Huawei 3Com Technologies Co.,Ltd.')
if mibBuilder.loadTexts: h3cQosCapability.setContactInfo('Platform Team Huawei 3Com Technologies Co.,Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085 ')
if mibBuilder.loadTexts: h3cQosCapability.setDescription('Huawei-3com QoS management information base.')
h3cQoSCapabilityMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1))
class CapabilityPhysicalType(TextualConvention, Integer32):
    reference = 'rfc2737 ENTITY-MIB '
    description = "An enumerated value which provides an indication of the general hardware type of a particular capability entity. The enumeration 'stack' is applicable if the physical entity class is some sort of super-container (possibly virtual), intended to group together multiple chassis entities. A stack may be realized by a 'virtual' cable, a real interconnect cable, attached to multiple chassis, or may in fact be comprised of multiple interconnect cables. A stack should not be modeled within any other physical entities, but a stack may be contained within another stack. Only chassis entities should be contained within a stack. The enumeration 'chassis' is applicable if the physical entity class is an overall container for networking equipment. Any class of physical entity except a stack may be contained within a chassis, and a chassis may only be contained within a stack. The enumeration 'module' is applicable if the physical entity class is some sort of self-contained sub-system. If it is removable, then it should be modeled within a container entity, otherwise it should be modeled directly within another physical entity (e.g., a chassis or another module). The enumeration 'port' is applicable if the physical entity class is some sort of networking port, capable of receiving and/or transmitting networking traffic. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("stack", 1), ("chassis", 2), ("module", 3), ("port", 4))

h3cQoSCapabilityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1))
h3cQoSCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1), )
if mibBuilder.loadTexts: h3cQoSCapabilityTable.setStatus('current')
if mibBuilder.loadTexts: h3cQoSCapabilityTable.setDescription('A table of capability of QoS of system information.')
h3cQoSCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalType"), (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCapabilityPhysicalIndex"), (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSModuleIndex"), (0, "A3COM-HUAWEI-QOS-CAPABILITY-MIB", "h3cQoSCharacteristicsIndex"))
if mibBuilder.loadTexts: h3cQoSCapabilityEntry.setStatus('current')
if mibBuilder.loadTexts: h3cQoSCapabilityEntry.setDescription('Capability of QoS information entry.')
h3cQoSCapabilityPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 1), CapabilityPhysicalType())
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalType.setStatus('current')
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalType.setDescription("The concentric device supports 'chassis' and 'port'. The distributed device supports 'chassis', 'module' and 'port'. The Intelligent Resilient Framework System supports 'stack', 'chassis', 'module' and 'port'. ")
h3cQoSCapabilityPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalIndex.setReference('RFC2737. RFC1213. ENTITY-MIB. ')
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: h3cQoSCapabilityPhysicalIndex.setDescription("Index of each physical entity. If h3cQoSCapabilityPhysicalType is 'stack', the value of this object is 0. If h3cQoSCapabilityPhysicalType is 'chassis' and 'module', the value of this object is equal to 'entPhysicalIndex', which is defined by 'ENTITY-MIB'. If h3cQoSCapabilityPhysicalType is 'port', the value of this object is equal to 'ifIndex', which is defined by 'RFC1213-MIB'. ")
h3cQoSModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: h3cQoSModuleIndex.setStatus('current')
if mibBuilder.loadTexts: h3cQoSModuleIndex.setDescription('The module index of QoS. QoS module: Index Characteristic 1 car module 2 gts module 3 lr module 4 hardware queue management module 5 wred module 6 priority mapping table module 7 colored priority mapping table module 8 port priority module 9 qos policy module 10 qos interface generic module 11 flow template module 12 vqos and vacl module 13 statistic module 21 carl module 22 fifo module 23 pq module 24 cq module 25 wfq module 26 rtpq module ')
h3cQoSCharacteristicsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: h3cQoSCharacteristicsIndex.setStatus('current')
if mibBuilder.loadTexts: h3cQoSCharacteristicsIndex.setDescription('The characteristics index of modules of QoS.')
h3cQoSCharacteristicsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 7, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSCharacteristicsValue.setStatus('current')
if mibBuilder.loadTexts: h3cQoSCharacteristicsValue.setDescription('The characteristics value of modules of QoS. The type of value of characteristics. car module: Index Characteristic Value 1 car function 1, if supported. 2 match any 1, if supported. 3 match acl If last 8 bits of this object are set to 1, it indicates that the match acl type is supported, bit 0 stands for IPv6 basic acl, bit 1 stands for IPv6 advanced acl, bit 2 stands for mac acl, bit 3 stands for user acl, bit 4 stands for IPv6 user acl, bit 5 stands for IPv6 simple acl, bit 6 stands for IPv4 basic acl, bit 7 stands for IPv4 advanced acl. 4 match carl 1, if supported. 5 green action If last 10 bits of this object are set to 1, it indicates that the green action type is supported, bit 0 stands for continue, bit 1 stands for drop, bit 2 stands for transmit, bit 3 stands for setting prec, bit 4 stands for setting dscp, bit 5 stands for setting exp, bit 6 stands for setting atm clp, bit 7 stands for setting fr de, bit 8 stands for setting 802.1p, bit 9 stands for setting local precedence. 6 yellow action If last 10 bits of this object are set to 1, it indicates that the yellow action type is supported, and the mask is same to green action. 7 red action If last 10 bits of this object are set to 1, it indicates that the red action type is supported, and the mask is same to green action. 8 input 1, if supported. 9 output 1, if supported. 10 cir 1, if supported. 11 burst size 1, if supported. 12 excess burst size 1, if supported. 13 pir 1, if supported. 14 default cir The default value of cir(integer). 15 lower limit of cir The lower limit value of cir(integer). 16 upper limit of cir The upper limit value of cir(integer). 17 cir granularity The value of cir granularity(integer). 18 default pir The default value of pir(integer). 19 lower limit of pir The lower limit value of cir(integer). 20 upper limit of pir The upper limit value of pir(integer). 21 pir granularity The value of pir granularity(integer). 22 default burst size The default value of burst size(integer). 23 lower limit of burst size The lower limit value of burst size(integer). 24 upper limit of burst size The upper limit value of burst size(integer). 25 car burst granularity size The value of burst granularity size(integer). 26 default excess burst size The default value of car excess burst size(integer). 27 lower limit of excess burst size The lower limit value of excess burst size(integer). 28 upper limit of excess burst size The upper limit value of excess burst size(integer). 29 excess burst granularity size The value of excess burst granularity size(integer). 30 car aggregation function 1, if supported. 31 max aggregation The max value of aggregation(integer). 32 flow number The value of flow number(integer). gts module Index Characteristic Value 1 gts function 1, if supported. 2 match any 1, if supported. 3 match acl If last 8 bits of this object are set to 1, it indicates that the match acl type is supported, bit 0 stands for IPv6 basic acl, bit 1 stands for IPv6 advanced acl, bit 2 stands for mac acl, bit 3 stands for user acl, bit 4 stands for IPv6 user acl, bit 5 stands for IPv6 simple acl, bit 6 stands for IPv4 basic acl, bit 7 stands for IPv4 advanced acl. 4 match queue 1, if supported. 5 cir 1, if supported. 6 burst size 1, if supported. 7 excess burst size 1, if supported. 8 queue length 1, if supported. 9 default cir The default value of cir(integer). 10 lower limit of cir The lower limit value of cir(integer). 11 upper limit of cir The upper limit value of cir(integer). 12 cir granularity The value of cir granularity(integer). 13 default burst size The default value of burst size(integer). 14 lower limit of burst size The lower limit value of burst size(integer). 15 upper limit of burst size The upper limit value of burst size(integer). 16 burst size granularity The value of burst size granularity(integer). 17 default excess burst size The default value of excess burst size(integer). 18 lower limit of excess burst size The lower limit value of excess burst size(integer). 19 upper limit of excess burst size The upper limit value of excess burst size(integer). 20 excess burst size granularity The value of excess burst size granularity(integer). 21 default queue length The default length of queue(integer). 22 lower limit of queue length The lower limit length of queue(integer). 23 upper limit of queue length The upper limit length of queue(integer). 24 queue number The number of queue(integer). 25 flow number The value of flow number(integer). 26 pir 1, if supported. 27 lower limit of pir The lower limit value of pir(integer). 28 upper limit of pir The upper limit value of pir(integer). 29 pir granularity The value of pir granularity(integer). lr module Index Characteristic Value 1 lr function 1, if supported. 2 input 1, if supported. 3 output 1, if supported. 4 cir 1, if supported. 5 burst size 1, if supported. 6 excess burst size 1, if supported. 7 default cir The default value of cir(integer). 8 lower limit of cir The lower limit value of cir(integer). 9 upper limit of cir The upper limit value of cir(integer). 10 cir granularity The value of cir granularity(integer). 11 default burst size The default value of burst size(integer). 12 lower limit of burst size The lower limit value of burst size(integer). 13 upper limit of burst size The upper limit value of burst size(integer). 14 burst size granularity The value of burst size granularity(integer). 15 default excess burst size The default value of excess burst size(integer). 16 lower limit of excess burst size The lower limit value of excess burst size(integer). 17 upper limit of excess burst size The upper limit value of excess burst size(integer). 18 excess burst size granularity The value of excess burst size granularity(integer). hardware queue management module Index Characteristic Value 1 hardware queue management function 1, if supported. 2 mode If last 7 bits of this object are set to 1, it indicates that the MODE type is supported, bit 0 stands for sp mode, bit 1 stands for wrr mode, bit 2 stands for hard wfq mode, bit 3 stands for sp pattern, bit 4 stands for max delay of wrr, bit 5 stands for wrr group, bit 6 stands for bandwidth mode. 3 default mode The default mode(integer). 4 max queue number The max number of queue(integer). 5 wrr group number The number of wrr group(integer). 6 wrr unit If last 2 bits of this object are set to 1, it indicates that the wrr unit type is supported, bit 0 stands for weight, bit 1 stands for byte count. 7 wfq unit If last 3 bits of this object are set to 1, it indicates that the wfq unit type is supported, bit 0 stands for bandwidth, bit 1 stands for percent, bit 2 stands for weight. 8 default wrr schedule value The default value of wrr schedule(integer). 9 lower limit of wrr schedule value The lower limit value of wrr schedule(integer). 10 upper limit of wrr schedule value The upper limit value of wrr schedule. 11 default value of wfq schedule The default value of wfq schedule(integer). 12 lower limit of wfq schedule value The lower limit value of wfq schedule(integer). 13 upper limit of wfq schedule value The upper limit value of wfq schedule. 14 default max delay The default value of max delay(integer). 15 lower limit of max delay The lower limit value of max delay(integer). 16 upper limit of max delay The upper limit value of max delay(integer). 17 wrr sp group 1, if supported. 18 wrr sp weight 1, if supported. 19 default wrr sp weight The default value of wrr sp weight(integer). 20 default wrr group The default group of wrr(integer). 21 default bandwidth value The default value of bandwidth(integer). 22 lower limit of bandwidth value The lower limit value of bandwidth(integer). 23 upper limit of bandwidth value The upper limit value of bandwidth(integer). wred module Index Characteristic Value 1 wred function 1, if supported. 2 port based 1, if supported. 3 table based The value of table based(integer). 4 IP precedence 1, if supported. 5 dscp 1, if supported. 6 exp 1, if supported. 7 atm clp 1, if supported. 8 802.1p 1, if supported. 9 fr de 1, if supported. 10 queue 1, if supported. 11 drop precedence 1, if supported. 12 color level If last 3 bits of this object are set to 1, it indicates that the color type is supported, bit 0 stands for green, bit 1 stands for yellow, bit 2 stands for red. 13 min threshold 1, if supported. 14 max threshold 1, if supported. 15 exponent 1, if supported. 16 discard probability denominator 1, if supported. 17 lower limit of min threshold The lower limit value of min threshold(integer). 18 upper limit of min threshold The upper limit value of min threshold(integer). 19 default min threshold The default value of min threshold(integer). 20 lower limit of max threshold The lower limit value of max threshold(integer). 21 lower limit of max threshold The upper limit value of max threshold(integer). 22 default max threshold The default value of max threshold (integer). 23 lower limit of exponent The lower limit value of exponent(integer). 24 upper limit of exponent The upper limit value of exponent(integer). 25 default exponent The default value of exponent(integer). 26 lower limit of discard probability denominator The lower limit value of mark prob(integer). 27 upper limit of discard probability denominator The upper limit value of mark prob(integer). 28 default discard probability denominator The value of default mark prob(integer). 29 port based parameter If last 2 bits of this object are set to 1, it indicates that the color type is supported, bit 0 stands for port based IP, bit 1 stands for port based dscp. priority mapping table module Index Characteristic Value 1 priority map table function 1, if supported. 2 802.1p map to lp If last 3 bits of this object are set to 1, it indicates that the direction type is supported, bit 0 stands for no direction, bit 1 stands for inbound, bit 2 stands for outbound. 3 802.1p map to dp Same to 802.1p map to lp. 4 802.1p map to dscp Same to 802.1p map to lp. 5 dscp map to lp Same to 802.1p map to lp. 6 dscp map to dp Same to 802.1p map to lp. 7 dscp map to 802.1p Same to 802.1p map to lp. 8 dscp map to dscp Same to 802.1p map to lp. 9 exp map to lp Same to 802.1p map to lp. 10 exp map to dp Same to 802.1p map to lp. 11 lp map to 802.1p Same to 802.1p map to lp. 12 802.1p map to rpr Same to 802.1p map to lp. 13 dscp map to rpr Same to 802.1p map to lp. 14 exp map to rpr Same to 802.1p map to lp. 15 IP precedence map to rpr Same to 802.1p map to lp. 16 lp map to dscp Same to 802.1p map to lp. 17 802.11e map to lp Same to 802.1p map to lp. 18 lp map to 802.11e Same to 802.1p map to lp. 19 up map to 802.1p Same to 802.1p map to lp. 20 up map to dscp Same to 802.1p map to lp. 21 up map to exp Same to 802.1p map to lp. 22 up map to dp Same to 802.1p map to lp. 23 up map to lp Same to 802.1p map to lp. 24 up map to rpr Same to 802.1p map to lp. 25 up map to fc Same to 802.1p map to lp. 26 lp map to lp Same to 802.1p map to lp. 27 802.1p map to exp Same to 802.1p map to lp. 28 dscp map to exp Same to 802.1p map to lp. 29 exp map to 802.1p Same to 802.1p map to lp. 30 exp map to dscp Same to 802.1p map to lp. 31 exp map to exp Same to 802.1p map to lp. 32 lp map to exp Same to 802.1p map to lp. 33 lp map to dp Same to 802.1p map to lp. 34 up map to up Same to 802.1p map to lp. colored priority mapping table module Index Characteristic Value 1 colored priority mapping table function If bit 0 - bit 2 of this object are set to 1, it indicates that the direction type is supported, bit 0 stands for no direction, bit 1 stands for inbound, bit 2 stands for outbound. If bit 3 - bit 5 of this object are set to 1, it indicates that the color type is supported, bit 3 stands for green, bit 4 stands for yellow, bit 5 stands for red. 2 802.1p map to lp Same to colored priority mapping table function. 3 802.1p map to dp Same to colored priority mapping table function. 4 802.1p map to dscp Same to colored priority mapping table function. 5 dscp map to lp Same to colored priority mapping table function. 6 dscp map to dp Same to colored priority mapping table function. 7 dscp map to 802.1p Same to colored priority mapping table function. 8 dscp map to dscp Same to colored priority mapping table function. 9 exp map to lp Same to colored priority mapping table function. 10 exp map to dp Same to colored priority mapping table function. 11 lp map to 802.1p Same to colored priority mapping table function. 12 802.1p map to rpr Same to colored priority mapping table function. 13 dscp map to rpr Same to colored priority mapping table function. 14 exp map to rpr Same to colored priority mapping table function. 15 IP precedence map to rpr Same to colored priority mapping table function. 16 lp map to dscp Same to colored priority mapping table function. 17 802.11e map to lp Same to colored priority mapping table function. 18 lp map to 802.11e Same to colored priority mapping table function. 19 up map to 802.1p Same to colored priority mapping table function. 20 up map to dscp Same to colored priority mapping table function. 21 up map to exp Same to colored priority mapping table function. 22 up map to dp Same to colored priority mapping table function. 23 up map to lp Same to colored priority mapping table function. 24 up map to rpr Same to colored priority mapping table function. 25 up map to fc Same to colored priority mapping table function. 26 lp map to lp Same to colored priority mapping table function. 27 802.1p map to exp Same to colored priority mapping table function. 28 dscp map to exp Same to colored priority mapping table function. 29 exp map to 802.1p Same to colored priority mapping table function. 30 exp map to dscp Same to colored priority mapping table function. 31 exp map to exp Same to colored priority mapping table function. 32 lp map to exp Same to colored priority mapping table function. 33 lp map to dp Same to colored priority mapping table function. 34 up map to up Same to colored priority mapping table function. port priority Module Index Characteristic Value 1 port priority function 1, if supported. 2 priority trust If last 2 bits of this object are set to 1, it indicates that the priority trust type is supported, bit 0 stands for global, bit 1 stands for interface. 3 802.1p 1, if supported. 4 dscp 1, if supported. 5 exp 1, if supported. 6 IP precedence 1, if supported. 7 802.11e 1, if supported. 8 override 1, if supported. 9 auto 1, if supported. qos policy module Index Characteristic Value 1 qos policy function If last 4 bits of this object are set to 1, it indicates that the policy type is supported, bit 0 stands for inbound, bit 1 stands for outbound, bit 2 stands for global inbound, bit 3 stands for global outbound. 2 match not 1, if supported. 3 and If last 19 bits of this object are set to 1, it indicates that the if match and type is supported, bit 0 stands for acl, bit 1 stands for class, bit 2 stands for dscp, bit 3 stands for inbound interface, bit 4 stands for IP precedence, bit 5 stands for rtp port, bit 6 stands for mpls exp, bit 7 stands for 802.1p, bit 8 stands for mac, bit 9 stands for protocol, bit 10 stands for service vlan ID, bit 11 stands for pr de, bit 12 stands for atm clp, bit 13 stands for source IP, bit 14 stands for any, bit 15 stands for local ID, bit 16 stands for topmost vlan, bit 17 stands for local precedence, bit 18 stands for drop priority. 4 or If last 19 bits of this object are set to 1, it indicates that the if match or type is supported, bit 0 stands for acl, bit 1 stands for class, bit 2 stands for dscp, bit 3 stands for inbound interface, bit 4 stands for IP precedence, bit 5 stands for rtp port, bit 6 stands for mpls exp, bit 7 stands for 802.1p, bit 8 stands for mac, bit 9 stands for protocol, bit 10 stands for service vlan ID, bit 11 stands for pr de, bit 12 stands for atm clp, bit 13 stands for source IP, bit 14 stands for any, bit 15 stands for local ID, bit 16 stands for topmost vlan, bit 17 stands for local precedence, bit 18 stands for drop priority. 5 match acl If last 8 bits of this object are set to 1, it indicates that the acl type is supported, bit 0 stands for IPv6 basic acl, bit 1 stands for IPv6 advanced acl, bit 2 stands for mac acl, bit 3 stands for user acl, bit 4 stands for IPv6 user acl, bit 5 stands for IPv6 simple acl, bit 6 stands for IPv4 basic acl, bit 7 stands for IPv4 advanced acl. 6 match sub class 1, if supported. 7 match dscp 1, if supported. 8 match inbound interface 1, if supported. 9 match ip precedence 1, if supported. 10 match rtp port 1, if supported. 11 match mpls exp 1, if supported. 12 match 802.1p 1, if supported. 13 match mac 1, if supported. 14 match protocol If last 3 bits of this object are set to 1, it indicates that the protocol type is supported, bit 0 stands for IPv4 protocol, bit 1 stands for IPv6 protocol, bit 2 stands for bittorrent protocol. 15 match customer vlan ID If last 2 bits of this object are set to 1, it indicates that the match type is supported, bit 0 stands for service vlan ID list, bit 1 stands for service vlan ID range. 16 match fr de 1, if supported. 17 match atm clp 1, if supported. 18 match source ip-address 1, if supported. 19 match any 1, if supported. 20 match qos local ID 1, if supported. 21 traffic police action 1, if supported. 22 traffic shape action 1, if supported. 23 set ip dscp action 1, if supported. 24 set ip precedence action 1, if supported. 25 set mpls exp action 1, if supported. 26 class based wfq action 1, if supported. 27 nest sub traffic policy 1, if supported. 28 set fr de action 1, if supported. 29 set 802.1p action 1, if supported. 30 set atm clp action 1, if supported. 31 account action 1, if supported. 32 filter action 1, if supported. 33 set drop priority action 1, if supported. 34 set vlan ID action 1, if supported. 35 traffic redirect to IP next hop 1, if supported. 36 traffic redirect to interface If last 11 bits of this object are set to 1, it indicates that the redirecting interface type is supported, bit 0 stands for l2ethernet, bit 1 stands for l2ge, bit 2 stands for l2xge, bit 3 stands for l3ethernet, bit 4 stands for l3ge, bit 5 stands for l3xge, bit 6 stands for serial, bit 7 stands for eacl, bit 8 stands for tunnel, bit 9 stands for olt, bit 10 stands for nat. 37 traffic redirect to cpu 1, if supported. 38 set local precedence action 1, if supported. 39 wred action 1, if supported. 40 set qos local ID action 1, if supported. 41 match service vlan ID If last 2 bits of this object are set to 1, it indicates that the match type is supported, bit 0 stands for service vlan list, bit 1 stands for service vlan range. 42 set service vlan ID 1, if supported. 43 nest topmost vlan tag If last 2 bits of this object are set to 1, it indicates that the nest type is supported, bit 0 stands for nest vlan ID, bit 1 stands for nest cos. 44 priority map action If last 21 bits of this object are set to 1, it indicates that the priority map type is supported, bit 0 stands for user def(Reserved right now), bit 1 stands for 802.1p map to lp, bit 2 stands for 802.1p map to dp, bit 3 stands for 802.1p map to dscp, bit 4 stands for dscp map to lp, bit 5 stands for dscp map to dp, bit 6 stands for dscp map to 802.1p, bit 7 stands for dscp map to dscp, bit 8 stands for exp map to lp, bit 9 stands for exp map to dp, bit 10 stands for lp map to 802.1p, bit 11 stands for lp map to lp, bit 12 stands for lp map to dscp, bit 13 stands for up map to 802.1p, bit 14 stands for up map to dscp, bit 15 stands for dscp map to exp, bit 16 stands for exp map to 802.1p, bit 17 stands for exp map to dscp, bit 18 stands for exp map to exp, bit 19 stands for lp map to exp, bit 20 stands for lp map to dp. 45 traffic redirect to aggregation group 1, if supported. 46 match local precedence 1, if supported. 47 match drop priority 1, if supported. 48 bind interface type not supported. 49 flow based mirror to interface If the bits of this object are set to 1, it indicates that the flow based mirror to interface type is supported. 50 flow based mirror to vlan 1, if supported. 51 flow based mirror to cpu 1, if supported. 52 qos policy support dynamic modified not supported. 53 set forwarding class ID action 1, if supported. 54 colored priority map action If last 22 bits of this object are set to 1, it indicates that the priority map type is supported, bit 0 stands for user def(Reserved right now), bit 1 stands for 802.1p map to lp, bit 2 stands for 802.1p map to dp, bit 3 stands for 802.1p map to dscp, bit 4 stands for dscp map to lp, bit 5 stands for dscp map to dp, bit 6 stands for dscp map to 802.1p, bit 7 stands for dscp map to dscp, bit 8 stands for exp map to lp, bit 9 stands for exp map to dp, bit 10 stands for lp map to 802.1p, bit 11 stands for lp map to lp, bit 12 stands for lp map to dscp, bit 13 stands for up map to 802.1p, bit 14 stands for up map to dscp, bit 15 stands for dscp map to exp, bit 16 stands for exp map to 802.1p, bit 17 stands for exp map to dscp, bit 18 stands for exp map to exp, bit 19 stands for lp map to exp, bit 20 stands for lp map to dp, bit 21 stands for color map dp. 55 802.1q manipulation mode If last 10 bits of this object are set to 1, it indicates that the 802.1q manipulation mode type is supported, bit 0 stands for behavior check method, bit 1 stands for behavior nest, bit 2 stands for behavior remark, bit 3 stands for classifier and, bit 4 stands for classifier or, bit 5 stands for classifier acl, bit 6 stands for classifier customer vlan, bit 7 stands for classifier service vlan, bit 8 stands for classifier customer 802.1p, bit 9 stands for classifier service 802,1p. 56 match service 802.1p 1, if supported. qos interface generic module Index Characteristic Value 1 hard If last 2 bits of this object are set to 1, it indicates that the qos port type is supported, bit 0 stands for soft, bit 1 stands for hard. 2 max bandwidth 1, if supported. 3 reserved bandwidth 1, if supported. 4 qm token 1, if supported. flow template module Index Characteristic Value 1 flow template function 1, if supported. 2 max number The max number of flow template(integer). 3 source IP address 1, if supported. 4 source IPv6 address 1, if supported. 5 destination IP address 1, if supported. 6 destination IPv6 address 1, if supported. 7 IP l3 protocol 1, if supported. 8 IPv6 l3 protocol 1, if supported. 9 dscp 1, if supported. 10 IPv6 dscp 1, if supported. 11 fragments 1, if supported. 12 IPv6 fragments 1, if supported. 13 source port 1, if supported. 14 destination port 1, if supported. 15 icmp type 1, if supported. 16 icmp code 1, if supported. 17 TCP flag 1, if supported. 18 source mac address 1, if supported. 19 source mac wildcast 1, if supported. 20 destination mac address 1, if supported. 21 destination mac wildcast 1, if supported. 22 eth protocol 1, if supported. 23 vlan ID 1, if supported. 24 cos 1, if supported. 25 cos service 1, if supported. 26 topmost vlan ID 1, if supported. 27 tos 1, if supported. 28 IPv6 tos 1, if supported. 29 IP precedence 1, if supported. 30 IPv6 precedence 1, if supported. 31 IPv6 icmp type 1, if supported. 32 IPv6 icmp code 1, if supported. 33 mpls exp 1, if supported. 46 offset type If last 7 bits of this object are set to 1, it indicates that the flow template extend offset type is supported, bit 0 stands for start, bit 1 stands for l2, bit 2 stands for mpls, bit 3 stands for IPv4, bit 4 stands for IPv6, bit 5 stands for l4, bit 6 stands for l5. 47 start offset The max value of start offset(integer). 48 start length The max value of start length(integer). 49 l2 offset The max value of l2 offset(integer). 50 l2 length The max value of l2 length(integer). 51 mpls offset The max value of mpls offset(integer). 52 mpls length The max value of mpls length(integer). 53 IPv4 offset The max value of IPv4 offset(integer). 54 IPv4 length The max value of IPv4 length(integer). 55 IPv6 offset The max value of IPv6 offset(integer). 56 IPv6 length The max value of IPv6 length(integer). 57 l4 offset The max value of l4 offset(integer). 58 l4 length The max value of l4 length(integer). 59 l5 offset The max value of l5 offset(integer). 60 l5 length The max value of l5 length(integer). vqos and vacl module Index Characteristic Value 1 vqos If last 2 bits of this object are set to 1, it indicates that the vqos and vacl type is supported, bit 0 stands for inbound, bit 1 stands for outbound. 2 vacl If last 2 bits of this object are set to 1, it indicates that the vacl type is supported, bit 0 stands for inbound, bit 1 stands for outbound. 3 vqos priority 1, if supported. Statistic Module Index Characteristic Value 1 current queue length statistic 1, if supported. 2 total queue length statistic 1, if supported. 3 queue drop pkt statistic 1, if supported. 4 current active wfq queue number statistic 1, if supported. 5 max number of active queue statistic 1, if supported. 6 total number of wfq queue statistic 1, if supported. 7 acl pkt number statistic 1, if supported. 8 acl byte number statistic 1, if supported. 9 car red pkt number statistic 1, if supported. 10 car red byte number statistic 1, if supported. 11 car green pkt number statistic 1, if supported. 12 car green byte number statistic 1, if supported. 13 car yellow pkt number statistic 1, if supported. 14 car yellow byte number statistic 1, if supported. 15 gts transmit pkt number statistic 1, if supported. 16 gts transmit byte number statistic 1, if supported. 17 gts delay pkt number statistic 1, if supported. 18 gts delay byte number statistic 1, if supported. 19 gts drop pkt number statistic 1, if supported. 20 gts drop byte number statistic 1, if supported. 21 lr transmit pkt number statistic 1, if supported. 22 lr transmit byte number statistic 1, if supported. 23 lr delay pkt number statistic 1, if supported. 24 lr delay pkt number statistic 1, if supported. 25 qos policy class match pkt statistic 1, if supported. 26 qos policy class match byte statistic 1, if supported. 27 account pkt number statistic 1, if supported. 28 account byte number statistic 1, if supported. 29 wred queue statistic 1, if supported. 30 wred precedence statistic 1, if supported. 31 wred green traffic statistic 1, if supported. 32 wred yellow traffic statistic 1, if supported. 33 wred red traffic statistic 1, if supported. 34 wred port based statistic 1, if supported. 35 hard interface queue statistic 1, if supported. carl module Index Characteristic Value 1 carl function 1, if supported. 2 match precedence 1, if supported. 3 match mac 1, if supported. 4 match dscp 1, if supported. fifo module Index Characteristic Value 1 fifo function 1, if supported. 2 set queue length 1, if supported. 3 default fifo queue length The value of default fifo queue length(integer). 4 lower limit of fifo queue length The lower limit value of fifo queue length(integer). 5 upper limit of fifo queue length The upper limit value of fifo queue length(integer). pq module Index Characteristic Value 1 pq function 1, if supported. 2 match pql 1, if supported. 3 pql function 1, if supported. 4 pql match inbound interface 1, if supported. 5 pql match protocol 1, if supported. 6 set pql default queue 1, if supported. 7 pql default queue The value of pql default queue(integer). 8 set pql queue length 1, if supported. 9 lower limit of pql queue length The lower limit value of pql queue length(integer). 10 upper limit of pql queue length The upper limit value of pql queue length(integer). 11 pql match local precedence 1, if supported. cq module Index Characteristic Value 1 cq function 1, if supported. 2 match cql 1, if supported. 3 cql function 1, if supported. 4 cql match inbound interface 1, if supported. 5 cql match protocol 1, if supported. 6 set cql default queue 1, if supported. 7 cql default queue The default queue of cql(integer). 8 set cql queue length 1, if supported. 9 cql queue serving 1, if supported. 10 default cql queue length The default length of cql queue(integer). 11 lower limit of cql queue length The lower limit value of cql queue length(integer). 12 upper limit of cql queue length The upper limit value of cql queue length(integer). 13 default cql queue serving The value of default cql queue serving(integer). 14 lower limit of cql queue serving The lower limit value of cql queue serving(integer). 15 upper limit of cql queue serving The upper limit value of cql queue serving(integer). 16 cql match local precedence 1, if supported. wfq module Index Characteristic Value 1 wfq function 1, if supported. 2 match dscp 1, if supported. 3 match precedence 1, if supported. 4 set wfq queue length 1, if supported. 5 set wfq queue number 1, if supported. 6 default wfq queue length The default length of wfq queue(integer). 7 lower limit of wfq queue length The lower limit value of wfq queue length(integer). 8 lower limit of wfq queue length The upper limit value of wfq queue length(integer). 9 default wfq queue number The default number of wfq queue(integer). 10 lower limit of wfq queue number The lower limit number of wfq queue(integer). 11 upper limit of wfq queue number The upper limit number of wfq queue(integer). 12 lower limit number of wfq queue based on dscp The lower limit number of wfq queue based on dscp(integer). 13 upper limit number of wfq queue based on dscp The upper limit number of wfq queue based on dscp(integer). rtpq module Index Characteristic Value 1 rtpq function 1, if supported. 2 match start port The value of match start port(integer). 3 match end port The value of match end port(integer). 4 bandwidth 1, if supported. 5 cbs 1, if supported. 6 default start port The value of default start port(integer). 7 lower limit of start port The lower limit value of start port(integer). 8 upper limit of start port The upper limit value of start port(integer). 9 default end port The value of default end port(integer). 10 lower limit of end port The lower limit value of end port(integer). 11 upper limit of end port The upper limit value of end port(integer). 12 default bandwidth The default value of bandwidth(integer). 13 lower limit of bandwidth The lower limit value of bandwidth(integer). 14 upper limit of bandwidth The upper limit value of bandwidth(integer). 15 default cbs The default value of cbs(integer). 16 lower limit of cbs The lower limit value of cbs(integer). 17 upper limit of cbs The upper limit value of cbs(integer). 18 queue length of low latency The queue length of low latency(integer). ')
mibBuilder.exportSymbols("A3COM-HUAWEI-QOS-CAPABILITY-MIB", h3cQosCapability=h3cQosCapability, CapabilityPhysicalType=CapabilityPhysicalType, PYSNMP_MODULE_ID=h3cQosCapability, h3cQoSCharacteristicsIndex=h3cQoSCharacteristicsIndex, h3cQoSCapabilityGroup=h3cQoSCapabilityGroup, h3cQoSCharacteristicsValue=h3cQoSCharacteristicsValue, h3cQoSCapabilityEntry=h3cQoSCapabilityEntry, h3cQoSCapabilityMibObjects=h3cQoSCapabilityMibObjects, h3cQoSCapabilityPhysicalType=h3cQoSCapabilityPhysicalType, h3cQoSModuleIndex=h3cQoSModuleIndex, h3cQoSCapabilityPhysicalIndex=h3cQoSCapabilityPhysicalIndex, h3cQoSCapabilityTable=h3cQoSCapabilityTable)
