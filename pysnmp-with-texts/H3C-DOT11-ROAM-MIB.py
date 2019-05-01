#
# PySNMP MIB module H3C-DOT11-ROAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DOT11-ROAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
h3cDot11, = mibBuilder.importSymbols("H3C-DOT11-REF-MIB", "h3cDot11")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, Unsigned32, MibIdentifier, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Integer32", "iso")
TruthValue, TextualConvention, DisplayString, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus", "MacAddress")
h3cDot11ROAM = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10))
h3cDot11ROAM.setRevisions(('2010-08-04 18:00', '2009-05-07 20:00', '2008-07-23 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cDot11ROAM.setRevisionsDescriptions(('Modified to add new h3cDot11RoamStatis2Group.', 'Modified to add new h3cDot11RoamStatisGroup.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cDot11ROAM.setLastUpdated('201008041800Z')
if mibBuilder.loadTexts: h3cDot11ROAM.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cDot11ROAM.setContactInfo('Platform Team Hangzhou H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R.China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cDot11ROAM.setDescription('This MIB provides information about WLAN roaming configuration. GLOSSARY IEEE 802.11 Standard to encourage interoperability among wireless networking equipment. Access point (AP) Transmitter/receiver (transceiver) device that commonly connects and transports data between a wireless network and a wired network. Access control (AC) To control and manage multi-APs, it will bridge wireless and wired network. BSS IEEE 802.11 Basic Service Set (Radio Cell). The BSS of an AP comprises of the stations directly associating with the AP. Radio The chip set to receive and send wireless signal. HA The AC to which a wireless station is connected by associating with an AP for the first time is the HA of the station. FA An AC that is other than the HA and to which a station is currently connected is an FA of the station. Fast-roam capable station A wireless station which directly associates to a fast-roam service (rsn+dot1X) with one AC for the first time. Roam-out station A wireless station which has associated with an AC other than the HA in the mobility-group is referred to as a roam-out station at its HA. Roam-in station A wireless station which has associated with an AC other than the HA in the mobility-group is referred to as a roam-in station at the FA. Intra-AC roaming A procedure where a wireless station roams from one AP to another AP, which are connected to the same AC. Inter-AC roaming A procedure where a wireless station roams from one AP to another AP, which are connected to different ACs. Inter-AC fast roaming capability If a station uses 802.1x (RSN) authentication through negotiation, this station has inter-AC fast roaming capability. WLAN-tunnel One type of layer 2 interface which is bound with an IACTP data tunnel and used to tunnel unicast/broadcast frames between ACs.')
class H3cDot11RoamMobileTunnelType(TextualConvention, Integer32):
    description = "The protocol type of the mobility-tunnel. This object has two defined values: - 'ipv4', which indicates that the protocol type of the mobility-tunnel is IPv4. - 'ipv6', which indicates that the protocol type of the mobility-tunnel is IPv6. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class H3cDot11RoamAuthMode(TextualConvention, Integer32):
    description = "The authentication mode of the mobility-tunnel. This object has two defined values: - 'none', which indicates that the authentication mode of the mobility-tunnel is None. - 'md5', which indicates that the authentication mode of the mobility-tunnel is MD5. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("md5", 2))

class H3cDot11RoamIACTPStatus(TextualConvention, Integer32):
    description = 'The status of IACTP state machine.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("init", 1), ("idle", 2), ("joinRequestWait", 3), ("joinResponseWait", 4), ("joinConfirmWait", 5), ("joinError", 6), ("run", 7))

h3cDot11RoamCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1))
h3cDot11RoamStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2))
h3cDot11RoamStatisGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 3))
h3cDot11RoamStatis2Group = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 4))
h3cDot11MobGrpTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1), )
if mibBuilder.loadTexts: h3cDot11MobGrpTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpTable.setDescription('The table defines the parameters for roaming group configuration.')
h3cDot11MobGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1), ).setIndexNames((0, "H3C-DOT11-ROAM-MIB", "h3cDot11MobGrpName"))
if mibBuilder.loadTexts: h3cDot11MobGrpEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpEntry.setDescription('This entry contains information of mobile group.')
h3cDot11MobGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15)))
if mibBuilder.loadTexts: h3cDot11MobGrpName.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpName.setDescription('Represents the name of roam group.')
h3cdot11MobGrpTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 2), H3cDot11RoamMobileTunnelType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cdot11MobGrpTunnelType.setStatus('current')
if mibBuilder.loadTexts: h3cdot11MobGrpTunnelType.setDescription('Represents the protocol type of mobility-tunnel.')
h3cDot11MobGrpSrcIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11MobGrpSrcIPAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpSrcIPAddr.setDescription('Represents the IP address of tunnel source. The IP address type must be the same as h3cdot11MobGrpTunnelType. The default value is zero.')
h3cDot11MobGrpAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 4), H3cDot11RoamAuthMode().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11MobGrpAuthMode.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpAuthMode.setDescription('Represents the authentication mode of IACTP tunnel. This object can be used to enable IACTP control message integrity authentication.')
h3cDot11MobGrpAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11MobGrpAuthKey.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpAuthKey.setDescription("Represents the authentication key of IACTP tunnel. Authentication key to be used with the given authentication method. This object can not be modified when the value of h3cDot11MobGrpAuthMode is 'none'.")
h3cDot11MobGrpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11MobGrpEnable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpEnable.setDescription("State of a mobile group. 'true' : The WLAN mobility group will be enabled. 'false' : The inter-AC tunnel communication for the mobility group will be disabled. A mobility group can be enabled only when the source IP address is configured. The other objects in this entry can become effective only when mobility group is enabled. The other objects in this entry can not be modified after enabling mobility group.")
h3cDot11MobGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11MobGrpRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpRowStatus.setDescription('The status of this table entry.')
h3cDot11MobGrpMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2), )
if mibBuilder.loadTexts: h3cDot11MobGrpMemberTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberTable.setDescription('The table defines the parameters for roaming member configuration.')
h3cDot11MobGrpMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2, 1), ).setIndexNames((0, "H3C-DOT11-ROAM-MIB", "h3cDot11MobGrpName"), (0, "H3C-DOT11-ROAM-MIB", "h3cDot11MobGrpMemberIpAddr"))
if mibBuilder.loadTexts: h3cDot11MobGrpMemberEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberEntry.setDescription('This entry contains information of mobile group member.')
h3cDot11MobGrpMemberIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2, 1, 1), InetAddress())
if mibBuilder.loadTexts: h3cDot11MobGrpMemberIpAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberIpAddr.setDescription('Represents the IP address of group member. It can not be the same as the source IP address of the mobile group. The address type must be the same as the h3cdot11MobGrpTunnelType.')
h3cDot11MobGrpMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2, 1, 2), H3cDot11RoamIACTPStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11MobGrpMemberStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberStatus.setDescription('Represents the status of group member.')
h3cDot11MobGrpMemberIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11MobGrpMemberIf.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberIf.setDescription('Represents the tunnel interface name of group member.')
h3cDot11MobGrpMemberUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2, 1, 4), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11MobGrpMemberUpTime.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberUpTime.setDescription('Represents the sustaining time from tunnel up. If tunnel is down, MemberUpTime is zero.')
h3cDot11MobGrpMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cDot11MobGrpMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cDot11MobGrpMemberRowStatus.setDescription('The status of this table entry.')
h3cDot11RoamInInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1), )
if mibBuilder.loadTexts: h3cDot11RoamInInfoTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamInInfoTable.setDescription('The table can used to display the information of roaming in client.')
h3cDot11RoamInInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1, 1), ).setIndexNames((0, "H3C-DOT11-ROAM-MIB", "h3cDot11RoamClientMAC"))
if mibBuilder.loadTexts: h3cDot11RoamInInfoEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamInInfoEntry.setDescription('This entry contains information of roaming in client.')
h3cDot11RoamClientMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: h3cDot11RoamClientMAC.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamClientMAC.setDescription('Represents the MAC address of roaming in client.')
h3cDot11RoamInClientBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamInClientBSSID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamInClientBSSID.setDescription('Represents BSSID of the AP to which the Roam-In client is associated.')
h3cDot11RoamInClientVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamInClientVlanID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamInClientVlanID.setDescription('Represents the VLAN ID of Roam-In client.')
h3cDot11RoamInHomeACIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamInHomeACIPType.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamInHomeACIPType.setDescription('Represents the protocol type of home AC address.')
h3cDot11RoamInHomeACIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamInHomeACIPAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamInHomeACIPAddr.setDescription('Represents the address of home AC.')
h3cDot11RoamOutInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2), )
if mibBuilder.loadTexts: h3cDot11RoamOutInfoTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutInfoTable.setDescription('The table can used to display the information of roaming out client.')
h3cDot11RoamOutInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2, 1), ).setIndexNames((0, "H3C-DOT11-ROAM-MIB", "h3cDot11RoamClientMAC"))
if mibBuilder.loadTexts: h3cDot11RoamOutInfoEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutInfoEntry.setDescription('This entry contains information of roaming out client.')
h3cDot11RoamOutClientBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamOutClientBSSID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutClientBSSID.setDescription('Represents the BSSID of the AP to which the Roam-Out client is associated.')
h3cDot11RoamOutClientVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamOutClientVlanID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutClientVlanID.setDescription('Represents the VLAN ID of Roam-Out client.')
h3cDot11RoamOutForeignACIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamOutForeignACIPType.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutForeignACIPType.setDescription('Represents the protocol type of foreign AC address.')
h3cDot11RoamOutForeignACIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamOutForeignACIPAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutForeignACIPAddr.setDescription('Represents the address of foreign AC.')
h3cDot11RoamOutClientUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 2, 1, 5), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamOutClientUpTime.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamOutClientUpTime.setDescription('Represents how long the Roam-Out client is associated with the foreign AC.')
h3cDot11RoamTrackTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3), )
if mibBuilder.loadTexts: h3cDot11RoamTrackTable.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackTable.setDescription("The table contains the roam-track information of a specified client on the client's HA.")
h3cDot11RoamTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1), ).setIndexNames((0, "H3C-DOT11-ROAM-MIB", "h3cDot11RoamTrackIndex"))
if mibBuilder.loadTexts: h3cDot11RoamTrackEntry.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackEntry.setDescription("This entry contains information of a specified client on the client's HA.")
h3cDot11RoamTrackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11RoamTrackIndex.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackIndex.setDescription('Represents the index of this entry.')
h3cDot11RoamTrackClientMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamTrackClientMAC.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackClientMAC.setDescription('Represents the MAC address of the roamed client.')
h3cDot11RoamTrackBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamTrackBSSID.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackBSSID.setDescription('Represents the BSSID of the AP with which the client is associated.')
h3cDot11RoamTrackUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1, 4), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamTrackUpTime.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackUpTime.setDescription('Represents how long the client is associated with the BSSID.')
h3cDot11RoamTrackACIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamTrackACIPType.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackACIPType.setDescription('Represents the protocol type of the IP address of the access controller with which the client is connected.')
h3cDot11RoamTrackACIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 2, 3, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RoamTrackACIPAddr.setStatus('current')
if mibBuilder.loadTexts: h3cDot11RoamTrackACIPAddr.setDescription('Represents the IP address of the access controller with which the client is connected.')
h3cDot11IntraACRoamingSuccCnt = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11IntraACRoamingSuccCnt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11IntraACRoamingSuccCnt.setDescription('Represents the count of client successfully roam Intra-AC.')
h3cDot11InterACRoamingSuccCnt = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11InterACRoamingSuccCnt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11InterACRoamingSuccCnt.setDescription('Represents the count of client successfully roam in Inter-AC.')
h3cDot11InterACRoamOutSuccCnt = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11InterACRoamOutSuccCnt.setStatus('current')
if mibBuilder.loadTexts: h3cDot11InterACRoamOutSuccCnt.setDescription('Represents the count of client successfully roam out Inter-AC.')
h3cDot11IntraACRoamingSuccCnt2 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11IntraACRoamingSuccCnt2.setStatus('current')
if mibBuilder.loadTexts: h3cDot11IntraACRoamingSuccCnt2.setDescription('Represents the count of client successfully roam Intra-AC in Counter32.')
h3cDot11InterACRoamingSuccCnt2 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11InterACRoamingSuccCnt2.setStatus('current')
if mibBuilder.loadTexts: h3cDot11InterACRoamingSuccCnt2.setDescription('Represents the count of client successfully roam in Inter-AC in Counter32.')
h3cDot11InterACRoamOutSuccCnt2 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 10, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11InterACRoamOutSuccCnt2.setStatus('current')
if mibBuilder.loadTexts: h3cDot11InterACRoamOutSuccCnt2.setDescription('Represents the count of client successfully roam out Inter-AC in Counter32.')
mibBuilder.exportSymbols("H3C-DOT11-ROAM-MIB", h3cDot11IntraACRoamingSuccCnt=h3cDot11IntraACRoamingSuccCnt, h3cDot11RoamTrackIndex=h3cDot11RoamTrackIndex, h3cDot11MobGrpMemberStatus=h3cDot11MobGrpMemberStatus, h3cDot11MobGrpName=h3cDot11MobGrpName, h3cDot11MobGrpMemberIpAddr=h3cDot11MobGrpMemberIpAddr, h3cDot11RoamTrackUpTime=h3cDot11RoamTrackUpTime, H3cDot11RoamMobileTunnelType=H3cDot11RoamMobileTunnelType, h3cDot11MobGrpMemberEntry=h3cDot11MobGrpMemberEntry, h3cDot11RoamTrackACIPAddr=h3cDot11RoamTrackACIPAddr, h3cDot11MobGrpMemberTable=h3cDot11MobGrpMemberTable, h3cDot11RoamStatis2Group=h3cDot11RoamStatis2Group, h3cDot11RoamTrackBSSID=h3cDot11RoamTrackBSSID, h3cDot11RoamClientMAC=h3cDot11RoamClientMAC, h3cDot11RoamTrackEntry=h3cDot11RoamTrackEntry, h3cDot11RoamOutClientBSSID=h3cDot11RoamOutClientBSSID, h3cDot11RoamInClientBSSID=h3cDot11RoamInClientBSSID, h3cDot11RoamInInfoTable=h3cDot11RoamInInfoTable, h3cDot11MobGrpMemberRowStatus=h3cDot11MobGrpMemberRowStatus, h3cDot11RoamTrackClientMAC=h3cDot11RoamTrackClientMAC, h3cDot11MobGrpMemberIf=h3cDot11MobGrpMemberIf, h3cdot11MobGrpTunnelType=h3cdot11MobGrpTunnelType, H3cDot11RoamAuthMode=H3cDot11RoamAuthMode, h3cDot11MobGrpSrcIPAddr=h3cDot11MobGrpSrcIPAddr, h3cDot11RoamOutClientUpTime=h3cDot11RoamOutClientUpTime, h3cDot11RoamOutInfoTable=h3cDot11RoamOutInfoTable, h3cDot11IntraACRoamingSuccCnt2=h3cDot11IntraACRoamingSuccCnt2, h3cDot11MobGrpAuthKey=h3cDot11MobGrpAuthKey, h3cDot11RoamStatisGroup=h3cDot11RoamStatisGroup, h3cDot11RoamInHomeACIPAddr=h3cDot11RoamInHomeACIPAddr, h3cDot11InterACRoamOutSuccCnt2=h3cDot11InterACRoamOutSuccCnt2, PYSNMP_MODULE_ID=h3cDot11ROAM, h3cDot11MobGrpMemberUpTime=h3cDot11MobGrpMemberUpTime, h3cDot11RoamInInfoEntry=h3cDot11RoamInInfoEntry, h3cDot11InterACRoamingSuccCnt=h3cDot11InterACRoamingSuccCnt, h3cDot11MobGrpEntry=h3cDot11MobGrpEntry, h3cDot11InterACRoamingSuccCnt2=h3cDot11InterACRoamingSuccCnt2, h3cDot11RoamOutInfoEntry=h3cDot11RoamOutInfoEntry, h3cDot11MobGrpAuthMode=h3cDot11MobGrpAuthMode, h3cDot11RoamTrackACIPType=h3cDot11RoamTrackACIPType, h3cDot11MobGrpTable=h3cDot11MobGrpTable, h3cDot11MobGrpEnable=h3cDot11MobGrpEnable, h3cDot11RoamOutClientVlanID=h3cDot11RoamOutClientVlanID, h3cDot11RoamInHomeACIPType=h3cDot11RoamInHomeACIPType, h3cDot11RoamInClientVlanID=h3cDot11RoamInClientVlanID, h3cDot11RoamOutForeignACIPAddr=h3cDot11RoamOutForeignACIPAddr, h3cDot11RoamTrackTable=h3cDot11RoamTrackTable, H3cDot11RoamIACTPStatus=H3cDot11RoamIACTPStatus, h3cDot11RoamOutForeignACIPType=h3cDot11RoamOutForeignACIPType, h3cDot11InterACRoamOutSuccCnt=h3cDot11InterACRoamOutSuccCnt, h3cDot11MobGrpRowStatus=h3cDot11MobGrpRowStatus, h3cDot11RoamStatusGroup=h3cDot11RoamStatusGroup, h3cDot11RoamCfgGroup=h3cDot11RoamCfgGroup, h3cDot11ROAM=h3cDot11ROAM)
