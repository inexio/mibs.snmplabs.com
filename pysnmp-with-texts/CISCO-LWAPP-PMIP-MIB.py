#
# PySNMP MIB module CISCO-LWAPP-PMIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-PMIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:06:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cldcClientMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, ObjectIdentity, Counter64, NotificationType, Counter32, Integer32, MibIdentifier, ModuleIdentity, Bits, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Counter64", "NotificationType", "Counter32", "Integer32", "MibIdentifier", "ModuleIdentity", "Bits", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
RowStatus, TimeStamp, TruthValue, TimeInterval, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TruthValue", "TimeInterval", "TextualConvention", "MacAddress", "DisplayString")
ciscoLwappPmipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 888))
ciscoLwappPmipMIB.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappPmipMIB.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappPmipMIB.setLastUpdated('201112220000Z')
if mibBuilder.loadTexts: ciscoLwappPmipMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappPmipMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappPmipMIB.setDescription("This MIB is intended to be implemented on all those devices operating as Central Controllers (CC) that terminate the Light Weight Access Point Protocol tunnel from Light-weight LWAPP Access Points. This MIB provides configuration and status information about local mobility anchor to which the controller has the joined. The relationship between CC and the LWAPP APs can be depicted as follows: +......+ +......+ +......+ +......+ + + + + + + + + + LMA + + LMA + + LMA + + LMA + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + WLC + + WLC + + WLC + + WLC + + WLC + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends it to the controller to which it is logically connected. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity also referred to as 'controller'. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. REFERENCE [1] Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications. [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol. ")
ciscoLwappPmipMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0))
ciscoLwappPmipGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1))
ciscoLwappPmipConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2))
ciscoLwappPmipStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3))
cLPmipDomainName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipDomainName.setStatus('current')
if mibBuilder.loadTexts: cLPmipDomainName.setDescription('This object specifies the domain name to which the controller belongs.')
cLPmipMAGInterface = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipMAGInterface.setStatus('current')
if mibBuilder.loadTexts: cLPmipMAGInterface.setDescription('This object specifies the interface to which the LMAs communicate.')
cLPmipMaxBindings = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipMaxBindings.setStatus('current')
if mibBuilder.loadTexts: cLPmipMaxBindings.setDescription('This object indicates the number of binding updates sent by the controller.')
cLPmipBindingLifeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 4), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingLifeTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipBindingLifeTime.setDescription('This object indicates the lifetime of the binding entries maintained by the controller.')
cLPmipBindingRefreshTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 5), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingRefreshTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipBindingRefreshTime.setDescription('This object indicates the refresh time for the binding entries maintained by the controller.')
cLPmipBindingInitRetxTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 6), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingInitRetxTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipBindingInitRetxTime.setDescription('This object indicates the initial timeout between proxy binding updates if the proxy binding ack does not arrive at the controller.')
cLPmipBindingMaxRetxTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 7), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingMaxRetxTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipBindingMaxRetxTime.setDescription('This object indicates the maximum timeout between proxy binding updates if the proxy binding ack does not arrive at the controller.')
cLPmipReplayProtectionTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 8), TimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipReplayProtectionTimestamp.setStatus('current')
if mibBuilder.loadTexts: cLPmipReplayProtectionTimestamp.setDescription('This object specifies the maximum amount of time difference between the timestamp in the received proxy binding ack and the current time of the day.')
cLPmipBriMinDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 9), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBriMinDelayTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipBriMinDelayTime.setDescription('This object specifies the minimum amount of time the controller should wait before retransmitting the BRI message.')
cLPmipBriMaxDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBriMaxDelayTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipBriMaxDelayTime.setDescription('This object specifies the maximum amount of time the controller should wait before retransmitting the BRI message.')
cLPmipBriRetries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBriRetries.setStatus('current')
if mibBuilder.loadTexts: cLPmipBriRetries.setDescription('This object specifies the maximum number of times the controller retransmits the BRI message before receiving the BRA message.')
cLPmipMagApnName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 12), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipMagApnName.setStatus('current')
if mibBuilder.loadTexts: cLPmipMagApnName.setDescription('This object specifies the MAG APN name for PMIPv6 MAG on AP.')
cLPmipLmaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1), )
if mibBuilder.loadTexts: cLPmipLmaTable.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaTable.setDescription('This table represents the information about the details of local mobility anchors connected to the controller.')
cLPmipLmaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipLmaName"))
if mibBuilder.loadTexts: cLPmipLmaEntry.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaEntry.setDescription('An entry in this table represents the details of local mobility anchors connected to the controller.')
cLPmipLmaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaName.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaName.setDescription('This object indicates the name of the LMA connected to the controller.')
cLPmipLmaIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaIPAddrType.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaIPAddrType.setDescription("This object indicates the LMA's IP address type, made available through cLPmipLmaIPAddr.")
cLPmipLmaIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaIPAddr.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaIPAddr.setDescription("This object indicates the LMA's IP address.")
cLPmipLmaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaRowStatus.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaRowStatus.setDescription('This object is used to add or delete an entry in this table.')
cLPmipLmaStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1), )
if mibBuilder.loadTexts: cLPmipLmaStatsTable.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaStatsTable.setDescription('This table represents the information about the LMAs that are connected to the controller.')
cLPmipLmaStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipLmaName"))
if mibBuilder.loadTexts: cLPmipLmaStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaStatsEntry.setDescription('Each entry in this table provides statistical information about the Local Mobility Anchors that are connected to the controller.')
cLPmipLmaTotalBindings = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaTotalBindings.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaTotalBindings.setDescription('This object represents total number of bindings sent to the LMA by the controller.')
cLPmipLmaPbuSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbuSent.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbuSent.setDescription('This object represents total number of proxy binding units sent to the LMA by the controller.')
cLPmipLmaPbaReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbaReceived.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbaReceived.setDescription('This object represents total number of proxy binding acks received for this LMA by the controller.')
cLPmipLmaPbriSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbriSent.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbriSent.setDescription('This object represents total number of pbri sent by the controller to the LMA')
cLPmipLmaPbriReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbriReceived.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbriReceived.setDescription('This object represents total number of pbri received from the LMA by the controller.')
cLPmipLmaPbraSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbraSent.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbraSent.setDescription('This object represents total number of pbra sent.')
cLPmipLmaPbraReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbraReceived.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbraReceived.setDescription('This object represents total number of pbra received.')
cLPmipLmaNoOfHandoff = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaNoOfHandoff.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaNoOfHandoff.setDescription('This object represents number of hand offs between the controller and the LMA.')
cLPmipLmaPbuDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbuDropped.setStatus('current')
if mibBuilder.loadTexts: cLPmipLmaPbuDropped.setDescription('This object represents number of pbus dropped between the controller and the LMA.')
cLPmipProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2), )
if mibBuilder.loadTexts: cLPmipProfileTable.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileTable.setDescription('This table represents the information about the details of PMIP profiles created on the controller.')
cLPmipProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileName"))
if mibBuilder.loadTexts: cLPmipProfileEntry.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileEntry.setDescription('An entry in this table represents the details of PMIP profiles created on the controller.')
cLPmipProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipProfileName.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileName.setDescription('This object indicates the name of the profile.')
cLPmipProfileNaiTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3), )
if mibBuilder.loadTexts: cLPmipProfileNaiTable.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileNaiTable.setDescription('This table represents the information about the details of PMIP profiles created in the controller.')
cLPmipProfileNaiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileName"), (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileNai"))
if mibBuilder.loadTexts: cLPmipProfileNaiEntry.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileNaiEntry.setDescription('An entry in this table represents the details of PMIP profiles created in the controller.')
cLPmipProfileNai = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileNai.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileNai.setDescription('This object indicates the name of the nai string assocaited with this profile.')
cLPmipProfileApn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileApn.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileApn.setDescription('This object indicates the name of the access point node connected to the controller.')
cLPmipProfileLmaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileLmaName.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileLmaName.setDescription('This object indicates the name of the LMA to which the profile is associated to.')
cLPmipProfileNaiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileNaiRowStatus.setStatus('current')
if mibBuilder.loadTexts: cLPmipProfileNaiRowStatus.setDescription('This object is used to add or delete an entry in this table.')
cLPmipWlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4), )
if mibBuilder.loadTexts: cLPmipWlanTable.setStatus('current')
if mibBuilder.loadTexts: cLPmipWlanTable.setDescription('This table represents the generic PMIP configuration for a particular WLAN in a controller. This table has a one-to-one relationship with cLWlanConfigTable. There exist a row in this table corresponding to each row representing a WLAN in cLWlanConfigTable.')
cLPmipWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLPmipWlanEntry.setStatus('current')
if mibBuilder.loadTexts: cLPmipWlanEntry.setDescription('Each entry in this table represents the generic PMIP configuration for a WLAN.')
cLPmipWlanProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipWlanProfileName.setStatus('current')
if mibBuilder.loadTexts: cLPmipWlanProfileName.setDescription('This object indicates the name of the profile associated to this WLAN.')
cLPmipWlanMobilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("pmipv6", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipWlanMobilityType.setStatus('current')
if mibBuilder.loadTexts: cLPmipWlanMobilityType.setDescription('This object specifies the mobility type of the clients associated to this particular WLAN.')
cLPmipWlanDefaultRealm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipWlanDefaultRealm.setStatus('current')
if mibBuilder.loadTexts: cLPmipWlanDefaultRealm.setDescription('This object indicates the name of the default realm associated to this WLAN.')
cLPmipClientInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2), )
if mibBuilder.loadTexts: cLPmipClientInfoTable.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientInfoTable.setDescription('This table represents the PMIP information of the clients associated to this controller.')
cLPmipClientInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cLPmipClientInfoEntry.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientInfoEntry.setDescription('Each entry in this table represents the generic PMIP information for a client.')
cLPmipClientNai = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientNai.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientNai.setDescription('This object indicates the name of the profile, the client is associated to.')
cLPmipClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientState.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientState.setDescription("This object indicates the state of the PMIP client: null: binding doesn't exist init: binding created, Retx timer running for PBU, binding not yet accepted from LMA, Tunnel/route is not yet setup active: binding accepted by LMA, refresh timer running, Tunnel/route setup complete. refreshPending: Refresh timer expired and Retx timer running. PBU refresh sent, PBA not yet received from LMA, (Tunnel/route is already setup). disconnectingSt: Dereg reply is expected. Retx timer is running, tunnel/route is still setup.")
cLPmipClientInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientInterface.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientInterface.setDescription('This object indicates the interface to which the client is associated.')
cLPmipClientHomeAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientHomeAddressType.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientHomeAddressType.setDescription("This object indicates the type of the Client's Home address made available through cLPmipClientHomeAddress.")
cLPmipClientHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientHomeAddress.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientHomeAddress.setDescription('This object indicates the Home Address of the client.')
cLPmipClientAtt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("reserved", 0), ("logicalNetworkInterface", 1), ("pointToPointInterface", 2), ("ethernet", 3), ("wirelessLan", 4), ("wimax", 5), ("threeGPPGERAN", 6), ("threeGPPUTRAN", 7), ("threeGPPETRAN", 8), ("threeGPP2eHRPD", 9), ("threeGPP2HRPD", 10), ("threeGPP21xRTT", 11), ("threeGPP2UMB", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientAtt.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientAtt.setDescription('This object indicates the access technology type by which the client is currently attached.')
cLPmipClientLocalLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientLocalLinkId.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientLocalLinkId.setDescription('This object indicates the local link identifier of the client.')
cLPmipClientLmaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientLmaName.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientLmaName.setDescription('This object indicates the LMA to which the client is connected.')
cLPmipClientLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientLifeTime.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientLifeTime.setDescription('This object indicates the duration of the PMIP client association.')
cLPmipClientDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientDomainName.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientDomainName.setDescription('This object indicates the domain to which the PMIP client is associated.')
cLPmipClientUpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientUpKey.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientUpKey.setDescription('This object indicates the upstream key of the PMIP client.')
cLPmipClientDownKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientDownKey.setStatus('current')
if mibBuilder.loadTexts: cLPmipClientDownKey.setDescription('This object indicates the downstream key of the PMIP client.')
mibBuilder.exportSymbols("CISCO-LWAPP-PMIP-MIB", cLPmipBindingRefreshTime=cLPmipBindingRefreshTime, cLPmipProfileTable=cLPmipProfileTable, cLPmipLmaStatsEntry=cLPmipLmaStatsEntry, cLPmipClientLocalLinkId=cLPmipClientLocalLinkId, cLPmipLmaPbraSent=cLPmipLmaPbraSent, cLPmipMaxBindings=cLPmipMaxBindings, cLPmipClientLifeTime=cLPmipClientLifeTime, cLPmipProfileLmaName=cLPmipProfileLmaName, cLPmipBindingLifeTime=cLPmipBindingLifeTime, cLPmipClientDomainName=cLPmipClientDomainName, cLPmipLmaName=cLPmipLmaName, cLPmipDomainName=cLPmipDomainName, cLPmipMagApnName=cLPmipMagApnName, cLPmipLmaStatsTable=cLPmipLmaStatsTable, cLPmipLmaPbuSent=cLPmipLmaPbuSent, cLPmipLmaPbriReceived=cLPmipLmaPbriReceived, cLPmipLmaIPAddrType=cLPmipLmaIPAddrType, ciscoLwappPmipConfig=ciscoLwappPmipConfig, cLPmipWlanMobilityType=cLPmipWlanMobilityType, cLPmipClientInterface=cLPmipClientInterface, PYSNMP_MODULE_ID=ciscoLwappPmipMIB, cLPmipProfileNaiEntry=cLPmipProfileNaiEntry, cLPmipLmaTable=cLPmipLmaTable, cLPmipMAGInterface=cLPmipMAGInterface, cLPmipClientDownKey=cLPmipClientDownKey, cLPmipLmaPbraReceived=cLPmipLmaPbraReceived, cLPmipLmaEntry=cLPmipLmaEntry, cLPmipClientLmaName=cLPmipClientLmaName, cLPmipBindingMaxRetxTime=cLPmipBindingMaxRetxTime, ciscoLwappPmipStatistics=ciscoLwappPmipStatistics, cLPmipProfileNai=cLPmipProfileNai, cLPmipLmaPbaReceived=cLPmipLmaPbaReceived, cLPmipLmaNoOfHandoff=cLPmipLmaNoOfHandoff, cLPmipClientUpKey=cLPmipClientUpKey, cLPmipLmaPbuDropped=cLPmipLmaPbuDropped, ciscoLwappPmipMIBObjects=ciscoLwappPmipMIBObjects, cLPmipReplayProtectionTimestamp=cLPmipReplayProtectionTimestamp, cLPmipClientAtt=cLPmipClientAtt, cLPmipBriRetries=cLPmipBriRetries, cLPmipProfileName=cLPmipProfileName, cLPmipLmaIPAddr=cLPmipLmaIPAddr, cLPmipLmaPbriSent=cLPmipLmaPbriSent, cLPmipLmaTotalBindings=cLPmipLmaTotalBindings, cLPmipWlanEntry=cLPmipWlanEntry, cLPmipProfileEntry=cLPmipProfileEntry, cLPmipClientState=cLPmipClientState, cLPmipClientNai=cLPmipClientNai, ciscoLwappPmipMIB=ciscoLwappPmipMIB, cLPmipBindingInitRetxTime=cLPmipBindingInitRetxTime, cLPmipWlanDefaultRealm=cLPmipWlanDefaultRealm, cLPmipBriMaxDelayTime=cLPmipBriMaxDelayTime, cLPmipProfileApn=cLPmipProfileApn, cLPmipProfileNaiRowStatus=cLPmipProfileNaiRowStatus, cLPmipBriMinDelayTime=cLPmipBriMinDelayTime, cLPmipLmaRowStatus=cLPmipLmaRowStatus, cLPmipProfileNaiTable=cLPmipProfileNaiTable, cLPmipWlanTable=cLPmipWlanTable, cLPmipClientInfoTable=cLPmipClientInfoTable, cLPmipClientInfoEntry=cLPmipClientInfoEntry, ciscoLwappPmipGlobal=ciscoLwappPmipGlobal, cLPmipWlanProfileName=cLPmipWlanProfileName, cLPmipClientHomeAddress=cLPmipClientHomeAddress, cLPmipClientHomeAddressType=cLPmipClientHomeAddressType)
