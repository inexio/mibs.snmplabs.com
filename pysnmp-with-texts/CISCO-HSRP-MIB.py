#
# PySNMP MIB module CISCO-HSRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HSRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:59:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, iso, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Bits, IpAddress, Counter32, ObjectIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "iso", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Bits", "IpAddress", "Counter32", "ObjectIdentity", "TimeTicks", "Unsigned32")
TruthValue, DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
ciscoHsrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 106))
ciscoHsrpMIB.setRevisions(('2010-09-06 00:00', '2005-12-20 00:00', '1998-08-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHsrpMIB.setRevisionsDescriptions(('The following changes have been made. [1] Objects cHsrpGrpIpNone has been added to the cHsrpGrpTable. [2] Added new object group cHsrpGrpGroupSup [3] Added new compliance cHsrpComplianceRev2, which deprecates cHsrpComplianceRev1.', 'Deprecated cHsrpCompliance and added cHsrpComplianceRev1 to include cHsrpNotificationsGroup; Updated the imports such that Unsigned32 is imported from SNMPv2-SMI instead of CISCO-TC, and other clean-up.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoHsrpMIB.setLastUpdated('201009060000Z')
if mibBuilder.loadTexts: ciscoHsrpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHsrpMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-hsrp@cisco.com')
if mibBuilder.loadTexts: ciscoHsrpMIB.setDescription("The MIB module provides a means to monitor and configure the Cisco IOS proprietary Hot Standby Router Protocol (HSRP). Cisco HSRP protocol is defined in RFC2281. Terminology: HSRP is a protocol used amoung a group of routers for the purpose of selecting an 'active router' and a 'standby router'. An 'active router' is the router of choice for routing packets. A 'standby router' is a router that takes over the routing duties when an active router fails, or when preset conditions have been met. An 'HSRP group' or a 'standby group' is a set of routers which communicate using HSRP. An HSRP group has a group MAC address and a group Virtual IP address. These are the designated addresses. The active router assumes (i.e. inherits) these group addresses. 'Hello' messages are sent to indicate that a router is running and is capable of becoming the active or standby router. 'Hellotime' is the interval between successive HSRP Hello messages from a given router. 'Holdtime' is the interval between the receipt of a Hello message and the presumption that the sending router has failed.")
class HsrpState(TextualConvention, Integer32):
    description = 'The current state of the HSRP protocol for a given HSRP group entry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 1), ("learn", 2), ("listen", 3), ("speak", 4), ("standby", 5), ("active", 6))

ciscoHsrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 1))
cHsrpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 1))
cHsrpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2))
cHsrpConfigTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cHsrpConfigTimeout.setStatus('current')
if mibBuilder.loadTexts: cHsrpConfigTimeout.setDescription('The amount of time in minutes a row in cHsrpGrpTable can remain in a state other than active before being timed out.')
cHsrpGrpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1), )
if mibBuilder.loadTexts: cHsrpGrpTable.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpTable.setDescription('A table containing information on each HSRP group for each interface.')
cHsrpGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-HSRP-MIB", "cHsrpGrpNumber"))
if mibBuilder.loadTexts: cHsrpGrpEntry.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpEntry.setDescription("Information about an HSRP group. Management applications use cHsrpGrpRowStatus to control entry modification, creation and deletion. Setting cHsrpGrpRowStatus to 'active' causes the router to communicate using HSRP. The value of cHsrpGrpRowStatus may be set to 'destroy' at any time. Entries may not be created via SNMP without explicitly setting cHsrpGrpRowStatus to either 'createAndGo' or 'createAndWait'. Entries can be created and modified via the management protocol or by the device's local management interface. A management application wishing to create an entry should choose the ifIndex of the interface which is to be added as part of an HSRP group. Also, a cHsrpGrpNumber should be chosen. A group number is unique only amongst the groups on a particular interface. The value of the group number appears in packets which are transmitted and received on a LAN segment to which the router is connected. The application must select the group number as explained in the description for cHsrpGrpNumber. If the row is not active, and a local management interface command modifies that row, the row may transition to active state. A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout.")
cHsrpGrpNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cHsrpGrpNumber.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpNumber.setDescription("This object along with the ifIndex of a particular interface uniquely identifies an HSRP group. Group numbers 0,1 and 2 are the only valid group numbers for TokenRing interfaces. For other media types, numbers range from 0 to 255. Each interface has its own set of group numbers. There's no relationship between the groups configured on different interfaces. Using a group number on one interface doesn't preclude using the same group number on a different interface. For example, there can be a group 1 on an Ethernet and a group 1 on Token Ring. More details can be found from RFC 2281.")
cHsrpGrpAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8)).clone('cisco')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpAuth.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpAuth.setDescription("This is an unencrypted authentication string which is carried in all HSRP messages. An authentication string mismatch prevents a router interface from learning the designated IP address or HSRP timer values from other HSRP-enabled routers with the same group number. The function of this object is not to supply any sort of security-like authentication but rather to confirm that what's happening is what's intended. In other words, this is meant for sanity checking only.")
cHsrpGrpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpPriority.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpPriority.setDescription('The cHsrpGrpPriority helps to select the active and the standby routers. The router with the highest priority is selected as the active router. In the priority range of 0 to 255, 0 is the lowest priority and 255 is the highest priority. If two (or more) routers in a group have the same priority, the one with the highest ip address of the interface is the active router. When the active router fails to send a Hello message within a configurable period of time, the standby router with the highest priority becomes the active router. A router with highest priority will only attempt to overthrow a lower priority active router if it is configured to preempt. But, if there is more than one router which is not active, the highest priority non-active router becomes the standby router.')
cHsrpGrpPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpPreempt.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpPreempt.setDescription('This object, if TRUE, indicates that the current router should attempt to overthrow a lower priority active router and attempt to become the active router. If this object is FALSE, the router will become the active router only if there is no such router (or if an active router fails).')
cHsrpGrpPreemptDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpPreemptDelay.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpPreemptDelay.setDescription("This delay is the time difference between a router power up and the time it can actually start preempting the currently active router. When a router first comes up, it doesn't have a complete routing table. If it's configured to preempt, then it will become the Active router, but it will not be able to provide adequate routing services. The solution to this is to allow for a configurable delay before the router actually preempts the currently active router.")
cHsrpGrpUseConfiguredTimers = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpUseConfiguredTimers.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpUseConfiguredTimers.setDescription("HSRP routers learn a group's Hellotime or Holdtime from hello messages. The Hellotime is used to determine the frequency of generating hello messages when this router becomes the active or standby router. The Holdtime is the interval between the receipt of a Hello message and the presumption that the sending router has failed. If this object is TRUE, the cHsrpGrpConfiguredHelloTime and cHsrpGrpConfiguredHoldTime will be used. If it is FALSE, the Hellotime and Holdtime values are learned.")
cHsrpGrpConfiguredHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 7), Unsigned32().clone(3000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpConfiguredHelloTime.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpConfiguredHelloTime.setDescription('If cHsrpGrpUseConfiguredTimers is true, cHsrpGrpConfiguredHelloTime is used when this router is an active router. Otherwise, the Hellotime learned from the current active router is used. All routers on a particular LAN segment must use the same Hellotime.')
cHsrpGrpConfiguredHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 8), Unsigned32().clone(10000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpConfiguredHoldTime.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpConfiguredHoldTime.setDescription('If cHsrpGrpUseConfiguredTimers is true, cHsrpGrpConfiguredHoldTime is used when this router is an active router. Otherwise, the Holdtime learned from the current active router is used. All routers on a particular LAN segment should use the same Holdtime. Also, the Holdtime should be at least three times the value of the Hellotime and must be greater than the Hellotime.')
cHsrpGrpLearnedHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 9), Unsigned32().clone(3000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpLearnedHelloTime.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpLearnedHelloTime.setDescription('If the Hellotime is not configured on a router, it can be learned from the Hello messages from active router, provided the Hello message is authenticated. If the Hellotime is not learned from a Hello message from the active router and it is not manually configured, a default value of 3 seconds is recommended.')
cHsrpGrpLearnedHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 10), Unsigned32().clone(10000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpLearnedHoldTime.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpLearnedHoldTime.setDescription('If the Holdtime is not configured on a router, it can be learned from the Hello message from the active router. Holdtime should be learned only if the Hello message is authenticated. If the Holdtime is not learned and it is not manually configured, a default value of 10 seconds is recommended.')
cHsrpGrpVirtualIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 11), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpVirtualIpAddr.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpVirtualIpAddr.setDescription('This is the primary virtual IP address used by this group. If this address is configured (i.e a non zero ip address), this value is used. Otherwise, the agent will attempt to discover the virtual address through a discovery process (which scans the hello messages).')
cHsrpGrpUseConfigVirtualIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpUseConfigVirtualIpAddr.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpUseConfigVirtualIpAddr.setDescription('If this object is TRUE, cHsrpGrpVirtualIpAddr was a configured one. Otherwise, it indicates that cHsrpGrpVirtualIpAddr was a learned one.')
cHsrpGrpActiveRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpActiveRouter.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpActiveRouter.setDescription('Ip Address of the currently active router for this group.')
cHsrpGrpStandbyRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpStandbyRouter.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpStandbyRouter.setDescription('Ip Address of the currently standby router for this group.')
cHsrpGrpStandbyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 15), HsrpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpStandbyState.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpStandbyState.setDescription('The current HSRP state of this group on this interface.')
cHsrpGrpVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 16), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cHsrpGrpVirtualMacAddr.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpVirtualMacAddr.setDescription('Mac Addresses used are as specified in RFC 2281. For ethernet and fddi interfaces, a MAC address will be in the range 00:00:0c:07:ac:00 through 00:00:0c:07:ac:ff. The last octet is the hexadecimal equivalent of cHsrpGrpNumber (0-255). Some Ethernet and FDDI interfaces allow a unicast MAC address for each HSRP group. Certain Ethernet chipsets(LANCE Ethernet, VGANYLAN and QUICC Ethernet) only support a single Unicast Mac Address. In this case, only one HSRP group is allowed. For TokenRing interfaces, the following three MAC addresses are permitted (functional addresses): C0:00:00:01:00:00 C0:00:00:02:00:00 C0:00:00:04:00:00.')
cHsrpGrpEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpEntryRowStatus.setDescription('The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpGrpEntry.')
cHsrpGrpIpNone = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cHsrpGrpIpNone.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpIpNone.setDescription('This object specifies the disable HSRP IPv4 virtual IP address.')
cHsrpMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 2))
cHsrpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 2, 0))
cHsrpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 106, 2, 0, 1)).setObjects(("CISCO-HSRP-MIB", "cHsrpGrpStandbyState"))
if mibBuilder.loadTexts: cHsrpStateChange.setStatus('current')
if mibBuilder.loadTexts: cHsrpStateChange.setDescription('A cHsrpStateChange notification is sent when a cHsrpGrpStandbyState transitions to either active or standby state, or leaves active or standby state. There will be only one notification issued when the state change is from standby to active and vice versa.')
cHsrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 3))
cHsrpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1))
cHsrpComplianceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2))
cHsrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1, 1)).setObjects(("CISCO-HSRP-MIB", "cHsrpConfigGroup"), ("CISCO-HSRP-MIB", "cHsrpGrpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpCompliance = cHsrpCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cHsrpCompliance.setDescription('The compliance statement for all hosts implementing the CISCO-HSRP-MIB.')
cHsrpComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1, 2)).setObjects(("CISCO-HSRP-MIB", "cHsrpConfigGroup"), ("CISCO-HSRP-MIB", "cHsrpGrpGroup"), ("CISCO-HSRP-MIB", "cHsrpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpComplianceRev1 = cHsrpComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: cHsrpComplianceRev1.setDescription('The object group is deprecated by the cHsrpComplianceRev2')
cHsrpComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1, 3)).setObjects(("CISCO-HSRP-MIB", "cHsrpConfigGroup"), ("CISCO-HSRP-MIB", "cHsrpGrpGroup"), ("CISCO-HSRP-MIB", "cHsrpGrpGroupSup"), ("CISCO-HSRP-MIB", "cHsrpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpComplianceRev2 = cHsrpComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: cHsrpComplianceRev2.setDescription('The compliance statement for all hosts implementing the CISCO-HSRP-MIB.')
cHsrpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 1)).setObjects(("CISCO-HSRP-MIB", "cHsrpConfigTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpConfigGroup = cHsrpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cHsrpConfigGroup.setDescription('The collection of objects used to set global configuration objects for the HSRP MIB.')
cHsrpGrpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 2)).setObjects(("CISCO-HSRP-MIB", "cHsrpGrpAuth"), ("CISCO-HSRP-MIB", "cHsrpGrpPriority"), ("CISCO-HSRP-MIB", "cHsrpGrpPreempt"), ("CISCO-HSRP-MIB", "cHsrpGrpPreemptDelay"), ("CISCO-HSRP-MIB", "cHsrpGrpUseConfiguredTimers"), ("CISCO-HSRP-MIB", "cHsrpGrpConfiguredHelloTime"), ("CISCO-HSRP-MIB", "cHsrpGrpConfiguredHoldTime"), ("CISCO-HSRP-MIB", "cHsrpGrpLearnedHelloTime"), ("CISCO-HSRP-MIB", "cHsrpGrpLearnedHoldTime"), ("CISCO-HSRP-MIB", "cHsrpGrpVirtualIpAddr"), ("CISCO-HSRP-MIB", "cHsrpGrpUseConfigVirtualIpAddr"), ("CISCO-HSRP-MIB", "cHsrpGrpActiveRouter"), ("CISCO-HSRP-MIB", "cHsrpGrpStandbyRouter"), ("CISCO-HSRP-MIB", "cHsrpGrpStandbyState"), ("CISCO-HSRP-MIB", "cHsrpGrpVirtualMacAddr"), ("CISCO-HSRP-MIB", "cHsrpGrpEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpGrpGroup = cHsrpGrpGroup.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpGroup.setDescription('The collection of objects used to add, delete and retrieve information about HSRP groups.')
cHsrpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 3)).setObjects(("CISCO-HSRP-MIB", "cHsrpStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpNotificationsGroup = cHsrpNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: cHsrpNotificationsGroup.setDescription('The collection of notifications used to indicate HSRP state information.')
cHsrpGrpGroupSup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 4)).setObjects(("CISCO-HSRP-MIB", "cHsrpGrpIpNone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cHsrpGrpGroupSup = cHsrpGrpGroupSup.setStatus('current')
if mibBuilder.loadTexts: cHsrpGrpGroupSup.setDescription('The collection of objects used to add, delete and retrieve information about HSRP groups.')
mibBuilder.exportSymbols("CISCO-HSRP-MIB", HsrpState=HsrpState, cHsrpGrpEntryRowStatus=cHsrpGrpEntryRowStatus, cHsrpGrpVirtualMacAddr=cHsrpGrpVirtualMacAddr, cHsrpGrpTable=cHsrpGrpTable, ciscoHsrpMIBObjects=ciscoHsrpMIBObjects, cHsrpGrpAuth=cHsrpGrpAuth, cHsrpGrpPreempt=cHsrpGrpPreempt, cHsrpGrpActiveRouter=cHsrpGrpActiveRouter, ciscoHsrpMIB=ciscoHsrpMIB, cHsrpStateChange=cHsrpStateChange, cHsrpGrpPreemptDelay=cHsrpGrpPreemptDelay, cHsrpConformance=cHsrpConformance, cHsrpConfigTimeout=cHsrpConfigTimeout, cHsrpGrpPriority=cHsrpGrpPriority, cHsrpGrpConfiguredHoldTime=cHsrpGrpConfiguredHoldTime, cHsrpGrpConfiguredHelloTime=cHsrpGrpConfiguredHelloTime, cHsrpComplianceRev2=cHsrpComplianceRev2, cHsrpGrpLearnedHelloTime=cHsrpGrpLearnedHelloTime, cHsrpGrpUseConfiguredTimers=cHsrpGrpUseConfiguredTimers, cHsrpGrpGroupSup=cHsrpGrpGroupSup, cHsrpGrpStandbyState=cHsrpGrpStandbyState, cHsrpCompliances=cHsrpCompliances, cHsrpNotificationsGroup=cHsrpNotificationsGroup, cHsrpGlobalConfig=cHsrpGlobalConfig, cHsrpMIBNotificationPrefix=cHsrpMIBNotificationPrefix, PYSNMP_MODULE_ID=ciscoHsrpMIB, cHsrpGrpGroup=cHsrpGrpGroup, cHsrpGrpNumber=cHsrpGrpNumber, cHsrpGrpEntry=cHsrpGrpEntry, cHsrpGrpIpNone=cHsrpGrpIpNone, cHsrpGrpStandbyRouter=cHsrpGrpStandbyRouter, cHsrpGrpVirtualIpAddr=cHsrpGrpVirtualIpAddr, cHsrpComplianceGroups=cHsrpComplianceGroups, cHsrpGrpLearnedHoldTime=cHsrpGrpLearnedHoldTime, cHsrpComplianceRev1=cHsrpComplianceRev1, cHsrpConfigGroup=cHsrpConfigGroup, cHsrpGroup=cHsrpGroup, cHsrpGrpUseConfigVirtualIpAddr=cHsrpGrpUseConfigVirtualIpAddr, cHsrpCompliance=cHsrpCompliance, cHsrpMIBNotifications=cHsrpMIBNotifications)
