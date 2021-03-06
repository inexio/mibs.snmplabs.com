#
# PySNMP MIB module HUAWEI-RPR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-RPR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
rprTopoImageIfIndex, rprTopoImageStationIfIndex, rprSpanId, rprTopoImageRinglet1Hops, rprSpanTotalRingletReservedRate, rprTopoImageWestProtectionStatus, rprIfIndex, RprSpan, rprTopoImageRinglet0Hops, rprIfRingOperModes, rprTopoImageEastProtectionStatus, rprSpanIfIndex, rprTopoImageMacAddress, rprIfCurrentStatus, rprIfWrapConfig, rprTopoImageStatus = mibBuilder.importSymbols("IEEE-802DOT17-RPR-MIB", "rprTopoImageIfIndex", "rprTopoImageStationIfIndex", "rprSpanId", "rprTopoImageRinglet1Hops", "rprSpanTotalRingletReservedRate", "rprTopoImageWestProtectionStatus", "rprIfIndex", "RprSpan", "rprTopoImageRinglet0Hops", "rprIfRingOperModes", "rprTopoImageEastProtectionStatus", "rprSpanIfIndex", "rprTopoImageMacAddress", "rprIfCurrentStatus", "rprIfWrapConfig", "rprTopoImageStatus")
ifName, ifPhysAddress, ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifPhysAddress", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity, MibIdentifier, Counter32, Counter64, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity", "MibIdentifier", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwRPR = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36))
if mibBuilder.loadTexts: hwRPR.setLastUpdated('200601090000Z')
if mibBuilder.loadTexts: hwRPR.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwRPR.setContactInfo(' R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwRPR.setDescription('The HUAWEI-RPR-TRAP-MIB contains objects to Monitor the RPR TRAPs. ********************************* RPR TRAP ********************************** This RPR TRAP consists of the following TRAPs: 1 : hwRPRexcessReservedRateDefect 2 : hwRPRprotMisconfigDefect 3 : hwRPRtopoChange 4 : hwRPRtopoInvalidDefect 5 : hwRPRduplicateMacAddressDefect 6 : hwRPRtopoInstabilityDefect 7 : hwRPRtopoStabilityRestore 8 : hwRPRPhyIfEventTrap 9 : hwRPRLogicIfEventTrap ')
hwRPRObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1))
hwRPRIfEventTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1), )
if mibBuilder.loadTexts: hwRPRIfEventTable.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfEventTable.setDescription('A table of interface event information.')
hwRPRIfEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1), ).setIndexNames((0, "HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"), (0, "HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"))
if mibBuilder.loadTexts: hwRPRIfEventEntry.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfEventEntry.setDescription('Interface event information Entry.')
hwRPRLogicIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwRPRLogicIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwRPRLogicIfIndex.setDescription('The ifIndex of this RPR logic interface.')
hwRPRLogicIfSpanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 2), RprSpan()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwRPRLogicIfSpanId.setStatus('current')
if mibBuilder.loadTexts: hwRPRLogicIfSpanId.setDescription('The SpanId of this RPR logic interface.')
hwRPRLogicIfEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sd", 1), ("sf", 2), ("mateerr", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwRPRLogicIfEvent.setStatus('current')
if mibBuilder.loadTexts: hwRPRLogicIfEvent.setDescription('Type of logic interface event. SD indicates that SDH Signal of the RPR logic interface degrades; SF indicates that SDH Signal of the RPR logic interface fails; MATEERR indicates that mate cable error caused by mate cable of the RPR physical interface is linked incorrect; ')
hwRPRPhyIfEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("sdHFramerSDst", 1), ("sdHFramerSFst", 2), ("sdHFramerLOSst", 3), ("sdHFramerLOFst", 4), ("sdHFramerRDIst", 5), ("sdHFramerAISst", 6), ("sdHFramerREIst", 7), ("miscabling", 8), ("keepalive", 9), ("mateState", 10)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwRPRPhyIfEvent.setStatus('current')
if mibBuilder.loadTexts: hwRPRPhyIfEvent.setDescription('Type of physical interface event. SDHFramerSDst indicates that SDH Signal of the RPR physical interface degrades; SDHFramerSFst indicates that SDH Signal of the RPR physical interface fails; SDHFramerLOSst indicates that SDH Signal of the RPR physical interface loses; SDHFramerLOFst indicates that SDH framer of the RPR physical interface loses; SDHFramerRDIst indicates that remote Defect Indication ; SDHFramerAISst indicates that alarm Indication Signal; SDHFramerREIst indicates that remote ErrorIndication; Miscabling indicates that cable of the RPR physical interface is linked incorrect; Keepalive indicates that an exchange of messages allowing verification that communication between stations is not active; MateState indicates that mate cable of the RPR physical interface is linked incorrect. ')
hwRPRIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2), )
if mibBuilder.loadTexts: hwRPRIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfConfigTable.setDescription('A table of RPR logic interface configuration information.')
hwRPRIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2, 1), ).setIndexNames((0, "HUAWEI-RPR-MIB", "hwRPRIfConfigIfIndex"))
if mibBuilder.loadTexts: hwRPRIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfConfigEntry.setDescription('RPR interface Configuration entry.')
hwRPRIfConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwRPRIfConfigIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfConfigIfIndex.setDescription('The ifIndex of this RPR logic interface.')
hwRPRLogicIfTotalBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1000, 2488, 10000))).clone(namedValues=NamedValues(("bandwidth1000", 1000), ("bandwidth2488", 2488), ("bandwidth10000", 10000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwRPRLogicIfTotalBandWidth.setStatus('current')
if mibBuilder.loadTexts: hwRPRLogicIfTotalBandWidth.setDescription('The total bandwidth of this RPR logic interface.')
hwRPRTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2))
hwRPRexcessReservedRateDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 1)).setObjects(("IEEE-802DOT17-RPR-MIB", "rprSpanTotalRingletReservedRate"))
if mibBuilder.loadTexts: hwRPRexcessReservedRateDefect.setStatus('current')
if mibBuilder.loadTexts: hwRPRexcessReservedRateDefect.setDescription('This defect indicates that the amount of reserved bandwidth on a ringlet exceeds the available LINK_RATE. When an excess reserved rate defect is present, a notification may be generated. ')
hwRPRprotMisconfigDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 2)).setObjects(("IEEE-802DOT17-RPR-MIB", "rprIfWrapConfig"), ("IEEE-802DOT17-RPR-MIB", "rprIfRingOperModes"))
if mibBuilder.loadTexts: hwRPRprotMisconfigDefect.setStatus('current')
if mibBuilder.loadTexts: hwRPRprotMisconfigDefect.setDescription('A critical severity defect that indicates the presence of mismatched-protection-configuration stations, based on the value returned by MismatchedProtection(). When a protection configuration defect is present on the station, a notification may be generated. ')
hwRPRtopoChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 3)).setObjects(("IEEE-802DOT17-RPR-MIB", "rprTopoImageStationIfIndex"), ("IEEE-802DOT17-RPR-MIB", "rprTopoImageStatus"), ("IEEE-802DOT17-RPR-MIB", "rprTopoImageWestProtectionStatus"), ("IEEE-802DOT17-RPR-MIB", "rprTopoImageEastProtectionStatus"), ("IEEE-802DOT17-RPR-MIB", "rprIfCurrentStatus"))
if mibBuilder.loadTexts: hwRPRtopoChange.setStatus('current')
if mibBuilder.loadTexts: hwRPRtopoChange.setDescription('When an topology change is present, a notification may be generated.. ')
hwRPRtopoInvalidDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 4)).setObjects(("IF-MIB", "ifPhysAddress"), ("IEEE-802DOT17-RPR-MIB", "rprIfCurrentStatus"))
if mibBuilder.loadTexts: hwRPRtopoInvalidDefect.setStatus('current')
if mibBuilder.loadTexts: hwRPRtopoInvalidDefect.setDescription('A critical severity defect indicating that an invalid entry has been found within the scope of the topology,the stations on the ring excess the MAX_STATIONS or the local station has one or more duplicate secondary MAC addresses. When a topology entry invalid defect ,exceeing MaxStations or duplicate secondary MAC addresses is present, a notification may be generated. ')
hwRPRduplicateMacAddressDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 5)).setObjects(("IF-MIB", "ifPhysAddress"), ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet0Hops"), ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet1Hops"))
if mibBuilder.loadTexts: hwRPRduplicateMacAddressDefect.setStatus('current')
if mibBuilder.loadTexts: hwRPRduplicateMacAddressDefect.setDescription('A critical severity defect indicating that a duplicateMacAddress has been found on the ring. When a duplicateMacAddress defect is present, a notification may be generated. ')
hwRPRtopoInstabilityDefect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 6)).setObjects(("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: hwRPRtopoInstabilityDefect.setStatus('current')
if mibBuilder.loadTexts: hwRPRtopoInstabilityDefect.setDescription('The critical severity Instable topology defect. When an Instable topology defect is present, a notification may be generated. ')
hwRPRtopoStabilityRestore = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 7)).setObjects(("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: hwRPRtopoStabilityRestore.setStatus('current')
if mibBuilder.loadTexts: hwRPRtopoStabilityRestore.setDescription('The critical severity Instable topology restore. When an stable topology is present, a notification may be generated. ')
hwRPRPhyIfEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 8)).setObjects(("HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"), ("HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"), ("HUAWEI-RPR-MIB", "hwRPRPhyIfEvent"))
if mibBuilder.loadTexts: hwRPRPhyIfEventTrap.setStatus('current')
if mibBuilder.loadTexts: hwRPRPhyIfEventTrap.setDescription('The critical severity physical interface defect. When an physical interface defect is present, a notification may be generated. ')
hwRPRLogicIfEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 9)).setObjects(("HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"), ("HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"), ("HUAWEI-RPR-MIB", "hwRPRLogicIfEvent"))
if mibBuilder.loadTexts: hwRPRLogicIfEventTrap.setStatus('current')
if mibBuilder.loadTexts: hwRPRLogicIfEventTrap.setDescription('The critical severity Logic interface defect. When an logic interface defect that caused by physical interface event is present, a notification may be generated. ')
hwRPRNodeConErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 10)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRNodeConErr.setStatus('current')
if mibBuilder.loadTexts: hwRPRNodeConErr.setDescription('On RPR ring, to detect the connection, a kind of packet is send between neighbor RPR nodes, This kind of packet is SC(Single-Choke) packet, If a node cannot receive SC packet from neighbor node in KEEPALIVE time, then there is failure between the two nodes. When happened, auto protection is executed by software.!')
hwRPRNodeConErrResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 11)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRNodeConErrResume.setStatus('current')
if mibBuilder.loadTexts: hwRPRNodeConErrResume.setDescription('On RPR ring, to detect the connection, a kind of packet is send between neighbor RPR nodes, This kind of packet is SC(Single-Choke) packet, If a node cannot receive SC packet from neighbor node in KEEPALIVE time, then there is failure between the two nodes. When failure is resumed , this notification is sent.!')
hwRPRNodeMisCabling = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 12)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRNodeMisCabling.setStatus('current')
if mibBuilder.loadTexts: hwRPRNodeMisCabling.setDescription('Optical fiber is connected in error. i.e the east direction of one node is connected with east direction of another node, or the west direction of one node is connected with west direction of another node!')
hwRPRNodeMisCablingResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 13)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRNodeMisCablingResume.setStatus('current')
if mibBuilder.loadTexts: hwRPRNodeMisCablingResume.setDescription('when phenomena that Optical fiber is connected in error disappears, this notification is sent!')
hwRPRMateErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 14)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRMateErr.setStatus('current')
if mibBuilder.loadTexts: hwRPRMateErr.setDescription('In double RPR operating mode, east and west directions of one rpr node lay on two RPR cards, These two cards are internally conntected by Gigaibit-ethernet, which is called MATE interface. The RPR nodes cannot work normaly under condition of MATE error.!')
hwRPRMateErrResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 15)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRMateErrResume.setStatus('current')
if mibBuilder.loadTexts: hwRPRMateErrResume.setDescription('In double RPR operating mode, east and west directions of one rpr node lay on two RPR cards, These two cards are internally conntected by Gigaibit-ethernet, which is called MATE interface. The RPR nodes cannot work normaly under condition of MATE error.when MATE error is resumed ,this notification is sent!')
hwRPRLOS = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 16)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRLOS.setStatus('current')
if mibBuilder.loadTexts: hwRPRLOS.setDescription("On RPR physical layer, link connection is detected through physical singal. When can't receive physical singal, then local node from neighbor node, LOS(lost of signal) alarm is report, auto protection is executed by software.!")
hwRPRLOSResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 17)).setObjects(("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwRPRLOSResume.setStatus('current')
if mibBuilder.loadTexts: hwRPRLOSResume.setDescription("On RPR physical layer, link connection is detected through physical singal. When can't receive physical singal, then local node from neighbor node, LOS(lost of signal) alarm is report, auto protection is executed by software.when LOS is resumed,this notification is sent")
hwRPRTrapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3))
hwRPRTrapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 1))
hwRPRTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 1, 1)).setObjects(("HUAWEI-RPR-MIB", "hwRPRIfEventGroup"), ("HUAWEI-RPR-MIB", "hwRPRTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRPRTrapCompliance = hwRPRTrapCompliance.setStatus('current')
if mibBuilder.loadTexts: hwRPRTrapCompliance.setDescription('The compliance statement for entities that implement RPRTRAP on a router. ')
hwRPRTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2))
hwRPRIfEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2, 1)).setObjects(("HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"), ("HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"), ("HUAWEI-RPR-MIB", "hwRPRPhyIfEvent"), ("HUAWEI-RPR-MIB", "hwRPRLogicIfEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRPRIfEventGroup = hwRPRIfEventGroup.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfEventGroup.setDescription('provide RPRTRAP objects configuration information. ')
hwRPRTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2, 2)).setObjects(("HUAWEI-RPR-MIB", "hwRPRexcessReservedRateDefect"), ("HUAWEI-RPR-MIB", "hwRPRprotMisconfigDefect"), ("HUAWEI-RPR-MIB", "hwRPRtopoChange"), ("HUAWEI-RPR-MIB", "hwRPRtopoInvalidDefect"), ("HUAWEI-RPR-MIB", "hwRPRduplicateMacAddressDefect"), ("HUAWEI-RPR-MIB", "hwRPRtopoInstabilityDefect"), ("HUAWEI-RPR-MIB", "hwRPRtopoStabilityRestore"), ("HUAWEI-RPR-MIB", "hwRPRPhyIfEventTrap"), ("HUAWEI-RPR-MIB", "hwRPRLogicIfEventTrap"), ("HUAWEI-RPR-MIB", "hwRPRNodeConErr"), ("HUAWEI-RPR-MIB", "hwRPRNodeConErrResume"), ("HUAWEI-RPR-MIB", "hwRPRNodeMisCabling"), ("HUAWEI-RPR-MIB", "hwRPRNodeMisCablingResume"), ("HUAWEI-RPR-MIB", "hwRPRMateErr"), ("HUAWEI-RPR-MIB", "hwRPRMateErrResume"), ("HUAWEI-RPR-MIB", "hwRPRLOS"), ("HUAWEI-RPR-MIB", "hwRPRLOSResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRPRTrapGroup = hwRPRTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwRPRTrapGroup.setDescription('Required objects to provide RPRTRAP objects configuration information. ')
hwRPRIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2, 3)).setObjects(("HUAWEI-RPR-MIB", "hwRPRLogicIfTotalBandWidth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRPRIfConfigGroup = hwRPRIfConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hwRPRIfConfigGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-RPR-MIB", hwRPRtopoStabilityRestore=hwRPRtopoStabilityRestore, hwRPRtopoInvalidDefect=hwRPRtopoInvalidDefect, hwRPRLOS=hwRPRLOS, hwRPRLogicIfTotalBandWidth=hwRPRLogicIfTotalBandWidth, hwRPRduplicateMacAddressDefect=hwRPRduplicateMacAddressDefect, hwRPRIfEventTable=hwRPRIfEventTable, hwRPRLogicIfIndex=hwRPRLogicIfIndex, hwRPRNodeConErrResume=hwRPRNodeConErrResume, hwRPRMateErrResume=hwRPRMateErrResume, hwRPRIfEventEntry=hwRPRIfEventEntry, hwRPRLOSResume=hwRPRLOSResume, hwRPRObjects=hwRPRObjects, hwRPRPhyIfEventTrap=hwRPRPhyIfEventTrap, hwRPRIfConfigEntry=hwRPRIfConfigEntry, hwRPRIfConfigTable=hwRPRIfConfigTable, hwRPRLogicIfSpanId=hwRPRLogicIfSpanId, hwRPR=hwRPR, hwRPRTraps=hwRPRTraps, PYSNMP_MODULE_ID=hwRPR, hwRPRexcessReservedRateDefect=hwRPRexcessReservedRateDefect, hwRPRNodeMisCabling=hwRPRNodeMisCabling, hwRPRTrapCompliance=hwRPRTrapCompliance, hwRPRTrapCompliances=hwRPRTrapCompliances, hwRPRPhyIfEvent=hwRPRPhyIfEvent, hwRPRTrapConformance=hwRPRTrapConformance, hwRPRTrapGroups=hwRPRTrapGroups, hwRPRIfEventGroup=hwRPRIfEventGroup, hwRPRprotMisconfigDefect=hwRPRprotMisconfigDefect, hwRPRIfConfigIfIndex=hwRPRIfConfigIfIndex, hwRPRLogicIfEventTrap=hwRPRLogicIfEventTrap, hwRPRNodeConErr=hwRPRNodeConErr, hwRPRIfConfigGroup=hwRPRIfConfigGroup, hwRPRTrapGroup=hwRPRTrapGroup, hwRPRtopoInstabilityDefect=hwRPRtopoInstabilityDefect, hwRPRLogicIfEvent=hwRPRLogicIfEvent, hwRPRNodeMisCablingResume=hwRPRNodeMisCablingResume, hwRPRtopoChange=hwRPRtopoChange, hwRPRMateErr=hwRPRMateErr)
