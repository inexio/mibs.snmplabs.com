#
# PySNMP MIB module ZXR10-SWITCHQOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-SWITCHQOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, enterprises, TimeTicks, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Integer32, IpAddress, Counter64, MibIdentifier, Unsigned32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "TimeTicks", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10switch = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102))
zxr10swqos = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3))
class DisplayString(OctetString):
    pass

class TrafficDropPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("low", 0), ("medium", 1), ("high", 2))

class TrafficColorMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("blind", 0), ("aware", 1))

class TrafficForward(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("forwardRed", 1))

class TrafficDrop(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dropYellow", 1))

class TrafficMirrorAction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cpu", 1), ("interface", 2))

class RedirectFlag(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cpu", 1), ("interface", 2), ("next-hop", 3), ("next-hop-ipv6", 4))

class Packettype(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("all", 0), ("red", 1), ("yellow", 2), ("green", 3))

class Statisticstype(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("packet", 0), ("byte", 1))

class GreenOnlyType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("green-only", 1))

class InetAddressIPv6(TextualConvention, OctetString):
    description = 'Represents an IPv6 network address: octets contents encoding 1-16 IPv6 address network-byte order 17-20 scope identifier network-byte order The corresponding InetAddressType value is ipv6(2). The scope identifier (bytes 17-20) MUST NOT be present for global IPv6 addresses. For non-global IPv6 addresses (e.g. link-local or site-local addresses), the scope identifier MUST always be present. It contains a link identifier for link-local and a site identifier for site-local IPv6 addresses. The scope identifier MUST disambiguate identical address values. For link-local addresses, the scope identifier will typically be the interface index (ifIndex as defined in the IF-MIB, RFC 2233) of the interface on which the address is configured. The scope identifier may contain the special value 0 which refers to the default scope. The default scope may be used in cases where the valid scope identifier is not known (e.g., a management application needs to write a site-local InetAddressIPv6 address without knowing the site identifier value). The default scope SHOULD NOT be used as an easy way out in cases where the scope identifier for a non-global IPv6 is known.'
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
zxr10AclQosPriorityMarkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1), )
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkTable.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkTable.setDescription('The description of zxr10 acl qos priority mark configuration. It is a list of acl qos priority mark entries.')
zxr10AclQosPriorityMarkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosPriorityMarkAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosPriorityMarkRuleId"))
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkEntry.setDescription('A acl qos Priority Mark entry containing objects that acl qos Priority Mark infomation,such as: dscp-value, dorp precedence etc.')
zxr10AclQosPriorityMarkAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkAclNo.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkAclNo.setDescription('The acl qos priority mark acl-number.')
zxr10AclQosPriorityMarkRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkRuleId.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkRuleId.setDescription('The acl qos priority mark rule-id.')
zxr10AclQosPriorityMarkAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkAclName.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkAclName.setDescription('The acl qos priority mark acl-name.')
zxr10AclQosPriorityMarkDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkDscpValue.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkDscpValue.setDescription('The acl qos priority mark dscp value, the valid value is 0-63')
zxr10AclQosPriorityMarkCosValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkCosValue.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkCosValue.setDescription('The acl qos priority mark cos value, the valid value is 0-7')
zxr10AclQosPriorityMarkLocalPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkLocalPrecedence.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkLocalPrecedence.setDescription('The acl qos priority mark local precedence value,the valid value is 0-7')
zxr10AclQosPriorityMarkDropPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 7), TrafficDropPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkDropPrecedence.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkDropPrecedence.setDescription('THe acl qos priority mark dorp precedence value, the valid value is high(2), low(0), medium(1)')
zxr10AclQosPriorityMarkOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkOuterVlanId.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkOuterVlanId.setDescription('The acl qos Priority Mark outer vlan id, the valid value is 1-4094.not support by 59 program')
zxr10AclQosPriorityMarkPrecedenceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkPrecedenceValue.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkPrecedenceValue.setDescription('The acl qos priority mark precedence value,the valid value is 0-7 ')
zxr10AclQosPriorityMarkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkRowStatus.setDescription('The acl qos Priority Mark item row status. if it is in valid status, it only can change to invalid status, no other status.when you creat something, you should enter creatAndGo(4), and when you want to delete it, you should enter destroy(6).')
zxr10AclQosTrafficLimitTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2), )
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitTable.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitTable.setDescription('The description of zxr10 acl qos traffic limit configuration. It is a list of acl qos traffic limit entries.')
zxr10AclQosTrafficLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficLimitAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficLimitRuleId"))
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitEntry.setDescription('A acl qos traffic limit entry containing objects that acl qos traffic limit infomation,such as: cbs value, ebs value, pir value, traffic limit mode etc.')
zxr10AclQosTrafficLimitAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitAclNo.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitAclNo.setDescription('The acl qos traffic limit acl number')
zxr10AclQosTrafficLimitRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRuleId.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRuleId.setDescription('The acl qos traffic limit rule id')
zxr10AclQosTrafficLimitAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitAclName.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitAclName.setDescription('The acl qos traffic limit acl name')
zxr10AclQosTrafficLimitCir = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitCir.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitCir.setDescription('The acl qos traffic limit cir value, the valid value is 1-32000000 in 89 program.but in 59 program is 64-32000000')
zxr10AclQosTrafficLimitCbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitCbs.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitCbs.setDescription('The acl qos traffic limit cbs value, the valid value is 1-16000.but in 59 program is 4-16000')
zxr10AclQosTrafficLimitEbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitEbs.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitEbs.setDescription('The acl qos traffic limit ebs value, the valid value is 4-16000.')
zxr10AclQosTrafficLimitPir = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitPir.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitPir.setDescription('The acl qos traffic limit pir value, the valid value is 64-32000000.')
zxr10AclQosTrafficLimitPbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitPbs.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitPbs.setDescription('The acl qos traffic limit pbs value, the valid value is 4-16000.')
zxr10AclQosTrafficLimitMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 9), TrafficColorMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitMode.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitMode.setDescription('The acl qos traffic limit work mode, the valid value is blind(0) or aware(1). ')
zxr10AclQosTrafficLimitRedDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRedDscpValue.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRedDscpValue.setDescription('The acl qos traffic limit red dscp value, the valid value is 0-63.')
zxr10AclQosTrafficLimitYelDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitYelDscpValue.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitYelDscpValue.setDescription('The acl qos traffic limit yellow dscp value, the valid value is 0-63.')
zxr10AclQosTrafficLimitRedDp = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 12), TrafficDropPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRedDp.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRedDp.setDescription('The acl qos traffic limit red drop, the valid value is high(2), low(0), medium(1).')
zxr10AclQosTrafficLimitYelDp = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 13), TrafficDropPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitYelDp.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitYelDp.setDescription('The acl qos traffic limit yellow drop,the valid value is high(2), low(0), medium(1). ')
zxr10AclQosTrafficLimitForwadRed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 14), TrafficForward()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitForwadRed.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitForwadRed.setDescription('The acl qos traffic forwad red,the valid value is forwad-red(1).')
zxr10AclQosTrafficLimitDropYellow = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 15), TrafficDrop()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitDropYellow.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitDropYellow.setDescription('The acl qos traffic limit drop yellow, the valid value is drop-yellow(1).')
zxr10AclQosTrafficLimitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRowStatus.setDescription('The acl qos Traffic Limit item row status. if it is in valid status, it only can change to invalid status, no other status.')
zxr10AclQosTrafficMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3), )
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorTable.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorTable.setDescription('The description of zxr10 acl qos traffic mirror configuration. It is a list of acl qos traffic mirror entries.')
zxr10AclQosTrafficMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficMirrorAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficMirrorRuleId"))
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorEntry.setDescription('A acl qos traffic mirror entry containing objects that acl qos traffic mirror infomation,such as: mirror action, interface name, row status etc.')
zxr10AclQosTrafficMirrorAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAclNo.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAclNo.setDescription('The acl qos traffic mirror acl number')
zxr10AclQosTrafficMirrorRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorRuleId.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorRuleId.setDescription('The acl qos traffic mirror ruler id')
zxr10AclQosTrafficMirrorAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAclName.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAclName.setDescription('The acl qos traffic mirror acl name')
zxr10AclQosTrafficMirrorAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 4), TrafficMirrorAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAction.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAction.setDescription('The acl qos traffic mirror action,cpu 1, interface 2')
zxr10AclQosTrafficMirrorIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorIfName.setDescription("when traffic mirror to interface, this is the interface's name. and this only for 59 program")
zxr10AclQosTrafficMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorRowStatus.setDescription('The acl qos Traffic Mirror item row status. if it is in valid status, it only can change to invalid status, no other status.when you creat something, you should enter creatAndGo(4), and when you want to delete it, you should enter destroy(6).')
zxr10AclQosRedirectTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4), )
if mibBuilder.loadTexts: zxr10AclQosRedirectTable.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectTable.setDescription('The description of zxr10 acl qos redirect configuration. It is a list of acl qos redirect entries.')
zxr10AclQosRedirectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosRedirectAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosRedirectRuleId"))
if mibBuilder.loadTexts: zxr10AclQosRedirectEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectEntry.setDescription('A acl qos redirect entry containing objects that acl qos redirect infomation,such as: globar port name, next-hop ip address, ip address priority etc.')
zxr10AclQosRedirectAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosRedirectAclNo.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectAclNo.setDescription('The acl qos redirect acl number')
zxr10AclQosRedirectRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosRedirectRuleId.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectRuleId.setDescription('The acl qos redirect Ruler id')
zxr10AclQosRedirectAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosRedirectAclName.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectAclName.setDescription('The acl qos redirect acl name')
zxr10AclQosRedirectFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 4), RedirectFlag()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectFlag.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectFlag.setDescription('The acl qos redirect flag,cpu 1, interface 2,next-hop 3, next-hop-ipv6(4)')
zxr10AclQosRedirectGPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectGPort.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectGPort.setDescription('The acl qos redirect interface name')
zxr10AclQosRedirectIpAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr1.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr1.setDescription('The first redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri1.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri1.setDescription('The priority of the firest ip address,0-7')
zxr10AclQosRedirectIpAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr2.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr2.setDescription('The second redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri2.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri2.setDescription('The priority of the second ip address,0-7')
zxr10AclQosRedirectIpAddr3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr3.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr3.setDescription('The third redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri3.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri3.setDescription('The priority of the third ip address,0-7')
zxr10AclQosRedirectIpAddr4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr4.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr4.setDescription('The fourth redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri4.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri4.setDescription('The priority of the fourth ip address,0-7')
zxr10AclQosRedirectIpAddr5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr5.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr5.setDescription('The fifth redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri5.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri5.setDescription('The priority of the fifth ip address,0-7')
zxr10AclQosRedirectIpAddr6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 16), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr6.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr6.setDescription('The sixth redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri6.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri6.setDescription('The priority of the sixth ip address,0-7')
zxr10AclQosRedirectIpAddr7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr7.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr7.setDescription('The seventh redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 19), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri7.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri7.setDescription('The priority of the seventh ip address,0-7')
zxr10AclQosRedirectIpAddr8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr8.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr8.setDescription('The eighth redirect next-hop ip adderss')
zxr10AclQosRedirectIpPri8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 21), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri8.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri8.setDescription('The priority of the eighth ip address,0-7')
zxr10AclQosRedirectIPv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 22), InetAddressIPv6()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIPv6Addr.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectIPv6Addr.setDescription(' The Redirect next-hop is IPv6 Address,support by 59 device.')
zxr10AclQosRedirectGreenOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 23), GreenOnlyType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectGreenOnly.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectGreenOnly.setDescription('The Redirect action only to green packet, support by 59 device.')
zxr10AclQosRedirectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 24), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosRedirectRowStatus.setDescription('The acl qos Redirect item row status. if it is in valid status, it only can change to invalid status, no other status.when you creat something, you should enter creatAndGo(4), and when you want to delete it, you should enter destroy(6).')
zxr10AclQosTrafficStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5), )
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsTable.setDescription('The description of zxr10 acl qos traffic statistics configuration. It is a list of acl qos traffic statistics entries.')
zxr10AclQosTrafficStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficStatisticsAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficStatisticsRuleId"))
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsEntry.setDescription('A acl qos traffic statistics entry containing objects that acl qos traffic statistics infomation,such as: pkt-type, statistics type etc.')
zxr10AclQosTrafficStatisticsAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsAclNo.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsAclNo.setDescription('The acl qos traffic Statistics acl number')
zxr10AclQosTrafficStatisticsRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsRuleId.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsRuleId.setDescription('The acl qos traffic Statistics ruler id')
zxr10AclQosTrafficStatisticsAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsAclName.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsAclName.setDescription('The acl qos traffic Statistics acl name')
zxr10AclQosTrafficStatisticsPkttype = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 4), Packettype()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsPkttype.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsPkttype.setDescription('The acl qos traffic Statistics pkt-type,all 0, green 1,red 2,yellow 3')
zxr10AclQosTrafficStatisticsStatype = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 5), Statisticstype()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsStatype.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsStatype.setDescription('The acl qos traffic Statistics statistics type :byte 1,packet 0')
zxr10AclQosTrafficStatisticsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsRowStatus.setDescription('The acl qos Traffic Statistics item row status. if it is in valid status, it only can change to invalid status, no other status.when you creat something, you should enter creatAndGo(4), and when you want to delete it, you should enter destroy(6).')
mibBuilder.exportSymbols("ZXR10-SWITCHQOS-MIB", zxr10AclQosTrafficMirrorTable=zxr10AclQosTrafficMirrorTable, zxr10AclQosTrafficStatisticsRuleId=zxr10AclQosTrafficStatisticsRuleId, zxr10AclQosRedirectAclNo=zxr10AclQosRedirectAclNo, zxr10AclQosTrafficLimitYelDscpValue=zxr10AclQosTrafficLimitYelDscpValue, zxr10AclQosTrafficLimitRedDp=zxr10AclQosTrafficLimitRedDp, zxr10AclQosRedirectIpPri2=zxr10AclQosRedirectIpPri2, zxr10AclQosRedirectEntry=zxr10AclQosRedirectEntry, zxr10AclQosTrafficMirrorAction=zxr10AclQosTrafficMirrorAction, zxr10AclQosPriorityMarkAclName=zxr10AclQosPriorityMarkAclName, zxr10AclQosTrafficStatisticsRowStatus=zxr10AclQosTrafficStatisticsRowStatus, zxr10AclQosRedirectAclName=zxr10AclQosRedirectAclName, TrafficDrop=TrafficDrop, zxr10AclQosRedirectIpAddr7=zxr10AclQosRedirectIpAddr7, TrafficMirrorAction=TrafficMirrorAction, zxr10AclQosTrafficMirrorAclNo=zxr10AclQosTrafficMirrorAclNo, zxr10AclQosTrafficLimitEbs=zxr10AclQosTrafficLimitEbs, InetAddressIPv6=InetAddressIPv6, zxr10AclQosTrafficLimitRowStatus=zxr10AclQosTrafficLimitRowStatus, GreenOnlyType=GreenOnlyType, zxr10AclQosTrafficLimitForwadRed=zxr10AclQosTrafficLimitForwadRed, zxr10AclQosRedirectRuleId=zxr10AclQosRedirectRuleId, zxr10AclQosTrafficStatisticsPkttype=zxr10AclQosTrafficStatisticsPkttype, zxr10AclQosRedirectIpAddr5=zxr10AclQosRedirectIpAddr5, zxr10AclQosTrafficMirrorEntry=zxr10AclQosTrafficMirrorEntry, zxr10AclQosTrafficLimitCir=zxr10AclQosTrafficLimitCir, zxr10AclQosTrafficMirrorRuleId=zxr10AclQosTrafficMirrorRuleId, zxr10AclQosPriorityMarkAclNo=zxr10AclQosPriorityMarkAclNo, zxr10AclQosRedirectIPv6Addr=zxr10AclQosRedirectIPv6Addr, zxr10AclQosRedirectGPort=zxr10AclQosRedirectGPort, zxr10AclQosTrafficLimitYelDp=zxr10AclQosTrafficLimitYelDp, zxr10AclQosRedirectIpPri4=zxr10AclQosRedirectIpPri4, zxr10AclQosTrafficLimitAclNo=zxr10AclQosTrafficLimitAclNo, TrafficForward=TrafficForward, zxr10AclQosRedirectIpAddr2=zxr10AclQosRedirectIpAddr2, zxr10AclQosTrafficLimitPbs=zxr10AclQosTrafficLimitPbs, zxr10AclQosRedirectRowStatus=zxr10AclQosRedirectRowStatus, zxr10AclQosPriorityMarkRowStatus=zxr10AclQosPriorityMarkRowStatus, zxr10AclQosPriorityMarkRuleId=zxr10AclQosPriorityMarkRuleId, zxr10AclQosTrafficLimitAclName=zxr10AclQosTrafficLimitAclName, zxr10AclQosRedirectIpPri3=zxr10AclQosRedirectIpPri3, zxr10AclQosRedirectFlag=zxr10AclQosRedirectFlag, zxr10AclQosRedirectIpPri5=zxr10AclQosRedirectIpPri5, zxr10AclQosTrafficLimitEntry=zxr10AclQosTrafficLimitEntry, zxr10AclQosRedirectGreenOnly=zxr10AclQosRedirectGreenOnly, RedirectFlag=RedirectFlag, zxr10AclQosRedirectIpAddr4=zxr10AclQosRedirectIpAddr4, zxr10AclQosRedirectIpAddr8=zxr10AclQosRedirectIpAddr8, zte=zte, zxr10AclQosTrafficStatisticsAclNo=zxr10AclQosTrafficStatisticsAclNo, zxr10AclQosPriorityMarkDscpValue=zxr10AclQosPriorityMarkDscpValue, zxr10AclQosRedirectIpAddr3=zxr10AclQosRedirectIpAddr3, zxr10AclQosPriorityMarkPrecedenceValue=zxr10AclQosPriorityMarkPrecedenceValue, zxr10AclQosTrafficMirrorAclName=zxr10AclQosTrafficMirrorAclName, zxr10AclQosPriorityMarkOuterVlanId=zxr10AclQosPriorityMarkOuterVlanId, zxr10AclQosTrafficLimitPir=zxr10AclQosTrafficLimitPir, TrafficColorMode=TrafficColorMode, zxr10AclQosTrafficLimitRedDscpValue=zxr10AclQosTrafficLimitRedDscpValue, zxr10AclQosTrafficStatisticsEntry=zxr10AclQosTrafficStatisticsEntry, zxr10AclQosRedirectIpPri7=zxr10AclQosRedirectIpPri7, zxr10AclQosRedirectTable=zxr10AclQosRedirectTable, zxr10AclQosTrafficLimitTable=zxr10AclQosTrafficLimitTable, zxr10AclQosRedirectIpPri6=zxr10AclQosRedirectIpPri6, zxr10AclQosTrafficMirrorIfName=zxr10AclQosTrafficMirrorIfName, zxr10AclQosRedirectIpPri1=zxr10AclQosRedirectIpPri1, Statisticstype=Statisticstype, zxr10AclQosTrafficMirrorRowStatus=zxr10AclQosTrafficMirrorRowStatus, zxr10AclQosRedirectIpPri8=zxr10AclQosRedirectIpPri8, zxr10AclQosTrafficLimitRuleId=zxr10AclQosTrafficLimitRuleId, Packettype=Packettype, TrafficDropPriority=TrafficDropPriority, zxr10AclQosTrafficLimitCbs=zxr10AclQosTrafficLimitCbs, zxr10AclQosTrafficStatisticsStatype=zxr10AclQosTrafficStatisticsStatype, zxr10AclQosPriorityMarkLocalPrecedence=zxr10AclQosPriorityMarkLocalPrecedence, zxr10AclQosTrafficStatisticsAclName=zxr10AclQosTrafficStatisticsAclName, zxr10AclQosPriorityMarkEntry=zxr10AclQosPriorityMarkEntry, zxr10AclQosPriorityMarkTable=zxr10AclQosPriorityMarkTable, zxr10=zxr10, zxr10swqos=zxr10swqos, zxr10AclQosPriorityMarkCosValue=zxr10AclQosPriorityMarkCosValue, zxr10AclQosTrafficLimitMode=zxr10AclQosTrafficLimitMode, zxr10AclQosPriorityMarkDropPrecedence=zxr10AclQosPriorityMarkDropPrecedence, zxr10AclQosRedirectIpAddr6=zxr10AclQosRedirectIpAddr6, DisplayString=DisplayString, zxr10AclQosTrafficLimitDropYellow=zxr10AclQosTrafficLimitDropYellow, zxr10switch=zxr10switch, zxr10AclQosTrafficStatisticsTable=zxr10AclQosTrafficStatisticsTable, zxr10AclQosRedirectIpAddr1=zxr10AclQosRedirectIpAddr1)
