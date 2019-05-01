#
# PySNMP MIB module WIRELESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WIRELESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
Timeticks, = mibBuilder.importSymbols("RFC1155-SMI", "Timeticks")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, Counter32, Gauge32, Unsigned32, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibmwlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 10))
wrBase = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 10, 1))
wrRemote = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 10, 2))
baseName = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseName.setStatus('mandatory')
if mibBuilder.loadTexts: baseName.setDescription('Name of the Base Station assigned through the Wireless Network Administration Program.')
baseNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseNetworkName.setStatus('mandatory')
if mibBuilder.loadTexts: baseNetworkName.setDescription('Name of the Wireless Network containing the Base Station. This name has been assigned through the Wireless Network Administration Program.')
baseAdminIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseAdminIPAddr.setStatus('mandatory')
if mibBuilder.loadTexts: baseAdminIPAddr.setDescription('IP Address of the station housing the Wireless Network Administration Program.')
wrBaseTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4), )
if mibBuilder.loadTexts: wrBaseTable.setStatus('mandatory')
if mibBuilder.loadTexts: wrBaseTable.setDescription('This table contains wireless interface parameters and state variables, one entry per wireless interface.')
wrBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1), ).setIndexNames((0, "WIRELESS-MIB", "baseIfIndex"))
if mibBuilder.loadTexts: wrBaseEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wrBaseEntry.setDescription('An entry contains wireless parameters and state variables for a particular interface.')
baseIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: baseIfIndex.setDescription('The value of this object identifies the wireless interface for which this entry contains management information. The value of this object for a particular interface has the same value as the IfIndex object defined in MIB-II for the same interface.')
baseHDLCaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseHDLCaddress.setStatus('mandatory')
if mibBuilder.loadTexts: baseHDLCaddress.setDescription('HDLC address of the wireless interface.')
baseNbOFRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseNbOFRemote.setStatus('mandatory')
if mibBuilder.loadTexts: baseNbOFRemote.setDescription('Number of wireless workstations registered to the wireless interface.')
baseCellIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseCellIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: baseCellIdentifier.setDescription('Identifier of the cell controlled by the wireless interface.')
baseAdapterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operational", 1), ("not-operational", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseAdapterStatus.setStatus('mandatory')
if mibBuilder.loadTexts: baseAdapterStatus.setDescription('Status of the wireless interface.')
baseEmittedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseEmittedPower.setStatus('mandatory')
if mibBuilder.loadTexts: baseEmittedPower.setDescription('Emitted power of the wireless interface.')
baseControllerCardDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseControllerCardDesc.setStatus('mandatory')
if mibBuilder.loadTexts: baseControllerCardDesc.setDescription('Vital Product Data of the wireless controller card performing the wireless interface function.')
baseUnivAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseUnivAddress.setStatus('mandatory')
if mibBuilder.loadTexts: baseUnivAddress.setDescription('Universal address of the wireless controller card performing the wireless interface function.')
baseModemDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseModemDesc.setStatus('mandatory')
if mibBuilder.loadTexts: baseModemDesc.setDescription('Vital Product Data of the transceiver performing the wireless interface function.')
baseTopologyTrapActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: baseTopologyTrapActive.setStatus('mandatory')
if mibBuilder.loadTexts: baseTopologyTrapActive.setDescription('Traps will be sent when wireless workstation registers to and deregisters from the wireless interface only if this object is set to active.')
wrBaseStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5), )
if mibBuilder.loadTexts: wrBaseStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: wrBaseStatsTable.setDescription('This table contains wireless interface statistics, one entry per wireless interface.')
wrBaseStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1), ).setIndexNames((0, "WIRELESS-MIB", "baseStatsIfIndex"))
if mibBuilder.loadTexts: wrBaseStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wrBaseStatsEntry.setDescription('An entry contains wireless statistics for a particular interface.')
baseStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsIfIndex.setDescription('The value of this object identifies the wireless interface for which this entry contains management information. The value of this object for a particular interface has the same value as the IfIndex object defined in MIB-II for the same interface.')
baseStatsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsXmit.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsXmit.setDescription('Number of packets transmitted over the wireless interface.')
baseStatsRxmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsRxmit.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsRxmit.setDescription('Number of packets retransmitted over the wireless interface due to a lack of positive acknowledgement.')
baseStatsNegAckRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsNegAckRcv.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsNegAckRcv.setDescription('Number of negative acknowledgement received over the wireless interface (workstations congestion indicator).')
baseStatsRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsRcv.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsRcv.setDescription('Number of packets received over the wireless interface.')
baseStatsLineErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsLineErrors.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsLineErrors.setDescription('Number of slots assigned to wireless workstations that fail to use or that fail to receive (HDLC error).')
baseStatsNegAckXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsNegAckXmit.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsNegAckXmit.setDescription('Number of negative acknowledgement transmitted over the wireless interface (base congestion indicator).')
baseStatsFramePurged = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsFramePurged.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsFramePurged.setDescription('Number of frames that were purged by the wireless interface because they were corrupted during air transmission.')
baseStatsFreqDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsFreqDelete.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsFreqDelete.setDescription('Number of times a single frequency had to be replaced in the frequency hopping pattern because an excessive level of interference was detected for that frequency.')
baseStatsHopAdvance = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsHopAdvance.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsHopAdvance.setDescription('Number of times a hop advance procedure had to be performed because an excessive level of interference was detected for each frequency of the hopping pattern.')
baseStatsCLineErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsCLineErrors.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsCLineErrors.setDescription('Number of times the first packet of a frame was received over the wireless interface with an HDLC error.')
baseStatsRcvICRFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsRcvICRFrame.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsRcvICRFrame.setDescription('Number of frames received by the base station on the wireless interface that must be forwarded to one or more wireless workstations registered to the same wireless interface.')
baseStatsXmitICRFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsXmitICRFrame.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsXmitICRFrame.setDescription('Number of frames forwarded by the base station from a wireless workstation to another one. This counter may be incremented several times for the same frame if it is a broadcast frame.')
baseStatsNoICRBufferAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsNoICRBufferAvail.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsNoICRBufferAvail.setDescription('Number of frames received on the wireless interface coming from a wireless workstation and going to another wireless workstation registered to the same wireless interface that had to be discarded due to a lack of resources.')
baseStatsNotRoutedICRFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsNotRoutedICRFrame.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsNotRoutedICRFrame.setDescription('Number of frames received on the wireless interface coming from a wireless workstation and going to another wireless workstation that were discarded because the target wireless workstation could not be found.')
baseStatsNbCUserEst = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 1, 5, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseStatsNbCUserEst.setStatus('mandatory')
if mibBuilder.loadTexts: baseStatsNbCUserEst.setDescription('Number of wireless workstation trying to transmit in C interval.')
wrRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1), )
if mibBuilder.loadTexts: wrRemoteTable.setStatus('mandatory')
if mibBuilder.loadTexts: wrRemoteTable.setDescription('This table contains management information for the wireless workstations registered to the wireless interfaces, one entry per registered wireless workstation.')
wrRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1), ).setIndexNames((0, "WIRELESS-MIB", "remIfIndex"), (0, "WIRELESS-MIB", "remIndex"))
if mibBuilder.loadTexts: wrRemoteEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wrRemoteEntry.setDescription('An entry contains management information for a particular wireless workstation. An object of this type is transient in that it ceases to exist when (or soon after) the wireless workstation deregisters from the base.')
remIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: remIfIndex.setDescription('The value of this object identifies the wireless interface to which is registered the workstation for which this entry contains management information. The value of this object for a particular interface has the same value as the IfIndex object defined in MIB-II for the same interface.')
remIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remIndex.setStatus('mandatory')
if mibBuilder.loadTexts: remIndex.setDescription('The value of this object identifies the registered wireless workstation for which this entry contains management information. This value has been dynamically assigned to the wireless workstation when it registered to the base.')
remMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remMacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: remMacAddress.setDescription('MAC address of the wireless workstation.')
remName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remName.setStatus('mandatory')
if mibBuilder.loadTexts: remName.setDescription('Name of the wireless workstation.')
remControllerCardDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remControllerCardDesc.setStatus('mandatory')
if mibBuilder.loadTexts: remControllerCardDesc.setDescription('Adapter Vital Product Data of the wireless workstation.')
remUnivAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remUnivAddress.setStatus('mandatory')
if mibBuilder.loadTexts: remUnivAddress.setDescription('Universal address of the wireless workstation.')
remModemDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remModemDesc.setStatus('mandatory')
if mibBuilder.loadTexts: remModemDesc.setDescription('Transceiver Vital Product Data of the wireless workstation.')
wrRemoteStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2), )
if mibBuilder.loadTexts: wrRemoteStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: wrRemoteStatsTable.setDescription('This table contains statistics information for the wireless workstations registered to the wireless interfaces, one entry per registered wireless workstation.')
wrRemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1), ).setIndexNames((0, "WIRELESS-MIB", "remStatsIfIndex"), (0, "WIRELESS-MIB", "remStatsIndex"))
if mibBuilder.loadTexts: wrRemStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wrRemStatsEntry.setDescription('An entry contains statistics information for a particular wireless workstation. An object of this type is transient in that it ceases to exist when (or soon after) the wireless workstation deregisters from the base.')
remStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsIfIndex.setDescription('The value of this object identifies the wireless interface to which is registered the workstation for which this entry contains management information. The value of this object for a particular interface has the same value as the IfIndex object defined in MIB-II for the same interface.')
remStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsIndex.setDescription('The value of this object identifies the wireless workstation for which this entry contains statistics information. This value has been dynamically assigned to the wireless workstation when it registered to the base.')
remStatsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsXmit.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsXmit.setDescription('Number of packets transmitted over the wireless interface to this particular wireless workstation.')
remStatsRxmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsRxmit.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsRxmit.setDescription('Number of packets retried over the wireless interface due to a lack of positive acknowledgement from this particular wireless workstation.')
remStatsNegAckRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsNegAckRcv.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsNegAckRcv.setDescription('Number of Out of Sequences Packets received over the wireless interface from this particular wireless workstation.')
remStatsRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsRcv.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsRcv.setDescription('Number of packets received over the wireless interface from this particular wireless workstation.')
remStatsLineErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsLineErrors.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsLineErrors.setDescription('Number of slots assigned to this particular wireless workstation that fail to use or that fail to receive (HDLC error).')
remStatsNegAckXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 10, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remStatsNegAckXmit.setStatus('mandatory')
if mibBuilder.loadTexts: remStatsNegAckXmit.setDescription('Number of negative acknowledgement transmitted to a given workstation over the wireless interface (base congestion indicator).')
mibBuilder.exportSymbols("WIRELESS-MIB", remMacAddress=remMacAddress, remStatsXmit=remStatsXmit, baseAdminIPAddr=baseAdminIPAddr, baseUnivAddress=baseUnivAddress, baseNetworkName=baseNetworkName, baseStatsRxmit=baseStatsRxmit, ibmwlan=ibmwlan, MacAddress=MacAddress, ibmProd=ibmProd, remIndex=remIndex, baseNbOFRemote=baseNbOFRemote, wrRemStatsEntry=wrRemStatsEntry, remControllerCardDesc=remControllerCardDesc, remStatsIfIndex=remStatsIfIndex, baseCellIdentifier=baseCellIdentifier, baseTopologyTrapActive=baseTopologyTrapActive, baseStatsXmit=baseStatsXmit, baseName=baseName, ibm=ibm, wrRemoteStatsTable=wrRemoteStatsTable, baseIfIndex=baseIfIndex, remStatsIndex=remStatsIndex, baseStatsRcv=baseStatsRcv, baseStatsLineErrors=baseStatsLineErrors, baseStatsNbCUserEst=baseStatsNbCUserEst, baseStatsFramePurged=baseStatsFramePurged, wrRemoteTable=wrRemoteTable, baseStatsIfIndex=baseStatsIfIndex, wrBaseEntry=wrBaseEntry, remStatsLineErrors=remStatsLineErrors, baseStatsNotRoutedICRFrame=baseStatsNotRoutedICRFrame, baseStatsHopAdvance=baseStatsHopAdvance, baseStatsNegAckRcv=baseStatsNegAckRcv, remName=remName, remStatsRxmit=remStatsRxmit, baseHDLCaddress=baseHDLCaddress, baseStatsCLineErrors=baseStatsCLineErrors, baseEmittedPower=baseEmittedPower, baseAdapterStatus=baseAdapterStatus, remStatsNegAckRcv=remStatsNegAckRcv, baseControllerCardDesc=baseControllerCardDesc, remUnivAddress=remUnivAddress, baseStatsFreqDelete=baseStatsFreqDelete, remModemDesc=remModemDesc, wrRemote=wrRemote, wrBaseStatsTable=wrBaseStatsTable, baseStatsNegAckXmit=baseStatsNegAckXmit, wrBaseStatsEntry=wrBaseStatsEntry, baseStatsRcvICRFrame=baseStatsRcvICRFrame, baseStatsXmitICRFrame=baseStatsXmitICRFrame, remStatsNegAckXmit=remStatsNegAckXmit, baseModemDesc=baseModemDesc, remStatsRcv=remStatsRcv, wrBase=wrBase, wrRemoteEntry=wrRemoteEntry, remIfIndex=remIfIndex, baseStatsNoICRBufferAvail=baseStatsNoICRBufferAvail, wrBaseTable=wrBaseTable)
