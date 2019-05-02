#
# PySNMP MIB module CISCO-DOT11-HT-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-MAC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Gauge32, Unsigned32, iso, TimeTicks, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Gauge32", "Unsigned32", "iso", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoDot11HtMacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 626))
ciscoDot11HtMacMIB.setRevisions(('2007-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setLastUpdated('200705160000Z')
if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setDescription("This MIB is intended to be implemented on Cisco's WLAN devices that provide the wired uplink to wireless clients through the high-throughput dot11 radios compliant to the 802.11n specification. The MIB describes the MAC layer parameters of the 802.11n compliant radio interfaces. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. A-MPDU An aggregated format that consists of several MAC Protocol Data Units being aggregated and transmitted in one PHY Service Data Unit. A-MSDU An aggregated format that consists of several MAC Service Data Units being aggregated and transmitted in one MAC Protocol Data Unit. Block-Ack This refers to the acknowledgement done for all the MPDUs in an A-MDPU. Basic Service Set ( BSS ) The IEEE 802.11 BSS of an AP comprises of the stations directly associating with the AP. Dual CTS Clear-To-Send control frame is sent by the receiver in response to the Request-To-Send (RTS) control frame from the sender to virtually reserve the wireless medium for data transfer. Dual CTS mechanism is used by the AP to reserve the wireless medium for wireless devices that do not support STBC. Green Field A mode of operation where high-throughput 802.11n frames are transmitted without a legacy compatible part. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. Mobile Node and client are used interchangeably. Modulation and Coding Scheme ( MCS ) This is a value that determines the modulation, coding and number of spatial channels. Each scheme specifies the modulation technique, coding rate , number of spatial streams etc and the corresponding data rate. Multiple Input Multiple Output ( MIMO ) This technique advocates sending and receiving data communication signals through multiple antennas. MIMO uses the multiple streams to transmit more information and recombine the signal at the receiving end. This brings more reliability and significant gain over the traditional antenna systems. Power Save Multi-Poll ( PSMP ) A MAC control frame that schedules the transmissions and receptions of PSMP-enabled devices. Phased Coexistence Operation ( PCO ) A BSS mode with alternating 20MHz and 40MHz phases of operation controlled by a PCO AP. Space-Time Block Coding ( STBC ) By this technique, a wireless device transmits several copies of a data stream across a series of antennas so that the receiver can use the various received portions of the data signal to improve reliability of data transfer. Reduced Inter-Frame Space ( RIFS ) A time interval between multiple transmissions of a single transmitter used to reduce overhead and increase network efficiency. TU A measurement of time equal to 1024 microseconds. REFERENCE [1] Part 11. Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications: Enhancements for Higher Throughput [2] Enhanced Wireless Consortium MAC Specification, v1.24 [3] Enhanced Wireless Consortium PHY Specification, v1.27 ")
ciscoDot11HtMacMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 0))
ciscoDot11HtMacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 1))
ciscoDot11HtMacMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 2))
cD11HtMacStationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1))
cD11HtMacOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2))
cD11HtMacStationConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1), )
if mibBuilder.loadTexts: cD11HtMacStationConfigTable.setReference('dot11PhyOperationTable, IEEE802dot11-MIB. ')
if mibBuilder.loadTexts: cD11HtMacStationConfigTable.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacStationConfigTable.setDescription("This table represents the MAC configuration parameters of 802.11n interfaces. There exists in this table, an entry corresponding to each entry in dot11PhyOperationTable where dot11PHYType equals 'ht'(7). ")
cD11HtMacStationConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtMacStationConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacStationConfigEntry.setDescription('Each Entry represents a conceptual row in ccD11HtMacStationConfigTable and corresponds to the MAC configuration parameters of an 802.11n interface. ')
cD11HtMacOperationalMCSSet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacOperationalMCSSet.setReference('Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications Section 7.2.3, Management Frames. ')
if mibBuilder.loadTexts: cD11HtMacOperationalMCSSet.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacOperationalMCSSet.setDescription('This object represents the set of MCS at which the station may transmit data. Each bit represents an MCS index and corresponds to a particular data rate. Each MCS shall be within the range from 0 to 127, and shall be supported for receiving data. This value is reported in transmitted Beacon, Probe Request, Probe Response, Association Request, Association Response, Reassociation Request and Reassociation Response frames and is used to indicate which MCS values shall be supported by all the devices in the BSS. When this object is zeroed, it indicates that the other stations in the BSS shall use legacy data rates. ')
cD11HtMacMIMOPowerSave = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("mimo", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMIMOPowerSave.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacMIMOPowerSave.setDescription("This object represents the operational power save state of MIMO. The semantics are defined as follows. 'static' - The dot11 interface is operating in static MIMO Power Save mode and hence, other stations should not send MIMO packets destined to this dot11 interface. 'dynamic'- The interface switches out of the MIMO Power Save mode to enable multiple receive chains when an RTS is received and switches back to the single receive-chain mode once the unicast transmission of the MPDU is complete. 'mimo' - The dot11 interface always has multiple receive-chains enabled and hence MIMO packets can always be sent to this interface. ")
cD11HtMacNDelayedBlockAckImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacNDelayedBlockAckImplemented.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacNDelayedBlockAckImplemented.setDescription("This object, when 'true', indicates that the dot11 interface supports the No-Ack option of the Delayed Block Acknowledgement. ")
cD11HtMacMaxAMSDULength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3839, 7935))).clone(namedValues=NamedValues(("amsduSize3839", 3839), ("amsduSize7935", 7935))).clone('amsduSize3839')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMaxAMSDULength.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacMaxAMSDULength.setDescription("This object represents the supported maximum size of A-MSDU. 'amsduSize3839' - This indicates a maximum size of 3839 octets. 'amsduSize7935' - This indicates a maximum size of 7935 octets. ")
cD11HtMacPSMPImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacPSMPImplemented.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPSMPImplemented.setDescription("This object, when 'true', indicates that the dot11 interface is capable of supporting PSMP. ")
cD11HtMacSTBCControlFrameImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacSTBCControlFrameImplemented.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacSTBCControlFrameImplemented.setDescription("This object, when 'true', indicates that the dot11 interface is capable of processing the received STBC control frames. ")
cD11HtMacLsigTxOpProtectImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacLsigTxOpProtectImplemented.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacLsigTxOpProtectImplemented.setDescription("This object, when 'true', indicates that the dot11 interface is capable of supporting L-SIG TXOP Protection option. ")
cD11HtMacMaxRxAMPDUFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMaxRxAMPDUFactor.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacMaxRxAMPDUFactor.setDescription('This object is used to compute the maximum length of the A-MPDU the STA can receive, as follows. maximum length of A-MPDU in octets = 2 ^ ( 13 + cD11HtMacMaxRxAMPDUFactor ) -1. ')
cD11HtMacMPDUDensity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noTimeRestriction", 1), ("oneEighth", 2), ("oneFourth", 3), ("half", 4), ("one", 5), ("two", 6), ("four", 7), ("eight", 8))).clone('one')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMPDUDensity.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacMPDUDensity.setDescription("This object represents the minimum time between the start of adjacent MPDUs within an A-MPDU. This time is measured at the PHY service access-point; the number of bytes between the start of two consecutive MPDUs in A-MPDU shall be equal or greater than (MPDU-density*PHY-bit-rate)/8. The encoding of the minimum time to this object is as follows. 'noTimeRestriction' - no time restriction between the start of adjacent MPDUs. 'oneEighth' - 1/8 microseconds 'oneFourth' - 1/4 microseconds 'half' - 1/2 microseconds 'one' - 1 microsecond 'two' - 2 microseconds 'four' - 4 microseconds 'eight' - 8 microseconds. ")
cD11HtMacPCOImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacPCOImplemented.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPCOImplemented.setDescription("This object, when 'true', indicates that the dot11 interface is capable of supporting Phased coexistence operation. ")
cD11HtMacTransitionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(400, 1500, 5000))).clone(namedValues=NamedValues(("fourHundred", 400), ("oneThousandFiveHundred", 1500), ("fiveThousand", 5000))).clone('fiveThousand')).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacTransitionTime.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacTransitionTime.setDescription('This object indicates that the minimum transition time within which the STA can switch between 20 MHz channel width and 40 MHz channel width with a high probability. ')
cD11HtMacMCSFeedbackImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("unsolicited", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMCSFeedbackImplemented.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacMCSFeedbackImplemented.setDescription("This object indicates the MCS feedback capability supported on this 802.11n interface. The semantics are as follows. 'none' - The station does not provide MCS feedback through this interface. 'unsolicited' - The station provides only unsolicited MCS feedback. 'both' - The station provides both solicited as well as unsolicited MCS feedback. ")
cD11HtMacAMSDUEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacAMSDUEnable.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacAMSDUEnable.setDescription('This object represents whether this 802.11n radio can transmit / receive A-MSDUs. ')
cD11HtMacAMPDUEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacAMPDUEnable.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacAMPDUEnable.setDescription('This object represents whether this 802.11n radio can transmit / receive A-MPDUs. ')
cD11HtMacOperationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1), )
if mibBuilder.loadTexts: cD11HtMacOperationTable.setReference('dot11PhyOperationTable, IEEE802dot11-MIB. ')
if mibBuilder.loadTexts: cD11HtMacOperationTable.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacOperationTable.setDescription("This table represents the operational parameters of 802.11n interfaces. Entries in this table are created automatically by the agent corresponding to each 802.11n interface. There exists in this table, an entry corresponding to each entry in dot11PhyOperationTable where dot11PHYType equals 'ht'(7). ")
cD11HtMacOperationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtMacOperationEntry.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacOperationEntry.setDescription('A conceptual row in cD11HtMacOperationTable and represents the operational parameters of an 802.11n interface. ')
cD11HtMacOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pureHt", 1), ("optionalProtection", 2), ("mandatoryFortyProtection", 3), ("mandatoryAllProtection", 4))).clone('pureHt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacOperatingMode.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacOperatingMode.setDescription("This object represents the level of protection to be provided to the data transmissions of 802.11n radios. The semantics are as follows. 'pureHt' - No protection will be provided to the high throughput tranmissions in the BSS started on this interface. This indicates that there will only be those high-throughput devices associated to the AP in the respective BSS. 'optionalProtection' - Protection is optional considering that there could be legacy devices in the control and extension channels. 'mandatoryFortyProtection' - Protection is mandatory for all the 40MHz channel transmissions. 'mandatoryAllProtection' - There are legacy devices in the BSS and hence all high throughput transmissions are mandatorily protected. ")
cD11HtMacRIFSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacRIFSMode.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacRIFSMode.setDescription("This object, when set to 'true', indicates that RIFS mode is allowed in the BSS. ")
cD11HtMacPSMPControlledAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPSMPControlledAccess.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPSMPControlledAccess.setDescription("This object, when set to 'true', indicates that the AP accepts associations only from PSMP-enabled clients. ")
cD11HtMacServiceIntervalGranularity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacServiceIntervalGranularity.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacServiceIntervalGranularity.setDescription('This object represents the service interval granularity to be used for scheduled PSMP. The value of the granularity is given by (cD11HtMacServiceIntervalGranularity+1)*5 milliseconds. ')
cD11HtMacDualCTSProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacDualCTSProtection.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacDualCTSProtection.setDescription("This object, when set to 'true', indicates that the AP uses dual CTS protection to protect the regular and the STBC transmissions. ")
cD11HtMacLSigTxOpFullProtectionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacLSigTxOpFullProtectionEnabled.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacLSigTxOpFullProtectionEnabled.setDescription("This object, when set to 'true', indicates that the LSIG-TXOP Protection is currently enabled on the AP. ")
cD11HtMacNonGFEntitiesPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacNonGFEntitiesPresent.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacNonGFEntitiesPresent.setDescription("This object, when set to 'true', indicates that Non-GreenField clients are present in the BSS. ")
cD11HtMacPCOActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCOActivated.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPCOActivated.setDescription("This object, when set to 'true', indicates that the PCO is activated. ")
cD11HtMacPCO20MaxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO20MaxDuration.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPCO20MaxDuration.setDescription('This object represents the maximum duration of 20 MHz phase in TU under PCO operation. The value of this object shall be equal to or larger than cD11HtMacPCO20MinDuration. ')
cD11HtMacPCO40MaxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO40MaxDuration.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPCO40MaxDuration.setDescription('This object represents the maximum duration of 40 MHz phase in TU under PCO operation. The value of this object shall be equal to or larger than cD11HtMacPCO40MinDuration. ')
cD11HtMacPCO20MinDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(40)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO20MinDuration.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPCO20MinDuration.setDescription('This object represents the minimum duration of 20 MHz phase in TU under PCO operation. ')
cD11HtMacPCO40MinDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(40)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO40MinDuration.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacPCO40MinDuration.setDescription('This object represents the minimum duration of 40 MHz phase in TU under PCO operation. ')
ciscoDot11HtMacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 1))
ciscoDot11HtMacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2))
cD11HtMacCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 1, 1)).setObjects(("CISCO-DOT11-HT-MAC-MIB", "ciscoDot11HtMacStationConfigGroup"), ("CISCO-DOT11-HT-MAC-MIB", "ciscoDot11HtMacOperationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cD11HtMacCompliance = cD11HtMacCompliance.setStatus('current')
if mibBuilder.loadTexts: cD11HtMacCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoDot11HtMacMIB module. ')
ciscoDot11HtMacStationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2, 1)).setObjects(("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacOperationalMCSSet"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMIMOPowerSave"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacNDelayedBlockAckImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMaxAMSDULength"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPSMPImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacSTBCControlFrameImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacLsigTxOpProtectImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMaxRxAMPDUFactor"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMPDUDensity"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCOImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacTransitionTime"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMCSFeedbackImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacAMSDUEnable"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacAMPDUEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtMacStationConfigGroup = ciscoDot11HtMacStationConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11HtMacStationConfigGroup.setDescription('This collection of objects represent the MAC configuration parameters of 802.11n radio interfaces. ')
ciscoDot11HtMacOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2, 2)).setObjects(("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacOperatingMode"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacRIFSMode"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPSMPControlledAccess"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacServiceIntervalGranularity"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacDualCTSProtection"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacLSigTxOpFullProtectionEnabled"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacNonGFEntitiesPresent"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCOActivated"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO40MaxDuration"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO20MaxDuration"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO40MinDuration"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO20MinDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtMacOperationsGroup = ciscoDot11HtMacOperationsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11HtMacOperationsGroup.setDescription('This collection of objects represent the MAC operational parameters of 802.11n radio interfaces. ')
mibBuilder.exportSymbols("CISCO-DOT11-HT-MAC-MIB", ciscoDot11HtMacOperationsGroup=ciscoDot11HtMacOperationsGroup, cD11HtMacStationConfigEntry=cD11HtMacStationConfigEntry, cD11HtMacNonGFEntitiesPresent=cD11HtMacNonGFEntitiesPresent, PYSNMP_MODULE_ID=ciscoDot11HtMacMIB, cD11HtMacNDelayedBlockAckImplemented=cD11HtMacNDelayedBlockAckImplemented, cD11HtMacAMPDUEnable=cD11HtMacAMPDUEnable, cD11HtMacServiceIntervalGranularity=cD11HtMacServiceIntervalGranularity, cD11HtMacPCO40MinDuration=cD11HtMacPCO40MinDuration, cD11HtMacStationConfig=cD11HtMacStationConfig, cD11HtMacTransitionTime=cD11HtMacTransitionTime, ciscoDot11HtMacStationConfigGroup=ciscoDot11HtMacStationConfigGroup, cD11HtMacPCO20MinDuration=cD11HtMacPCO20MinDuration, cD11HtMacSTBCControlFrameImplemented=cD11HtMacSTBCControlFrameImplemented, cD11HtMacOperationTable=cD11HtMacOperationTable, ciscoDot11HtMacMIBNotifs=ciscoDot11HtMacMIBNotifs, cD11HtMacOperationalMCSSet=cD11HtMacOperationalMCSSet, cD11HtMacPCO20MaxDuration=cD11HtMacPCO20MaxDuration, cD11HtMacCompliance=cD11HtMacCompliance, cD11HtMacOperatingMode=cD11HtMacOperatingMode, ciscoDot11HtMacMIBConform=ciscoDot11HtMacMIBConform, cD11HtMacPSMPImplemented=cD11HtMacPSMPImplemented, cD11HtMacRIFSMode=cD11HtMacRIFSMode, cD11HtMacStationConfigTable=cD11HtMacStationConfigTable, cD11HtMacLSigTxOpFullProtectionEnabled=cD11HtMacLSigTxOpFullProtectionEnabled, cD11HtMacLsigTxOpProtectImplemented=cD11HtMacLsigTxOpProtectImplemented, cD11HtMacAMSDUEnable=cD11HtMacAMSDUEnable, cD11HtMacMIMOPowerSave=cD11HtMacMIMOPowerSave, ciscoDot11HtMacMIBCompliances=ciscoDot11HtMacMIBCompliances, cD11HtMacOperationEntry=cD11HtMacOperationEntry, cD11HtMacPCOImplemented=cD11HtMacPCOImplemented, cD11HtMacMPDUDensity=cD11HtMacMPDUDensity, ciscoDot11HtMacMIBGroups=ciscoDot11HtMacMIBGroups, cD11HtMacOperations=cD11HtMacOperations, cD11HtMacPCO40MaxDuration=cD11HtMacPCO40MaxDuration, ciscoDot11HtMacMIB=ciscoDot11HtMacMIB, cD11HtMacMaxRxAMPDUFactor=cD11HtMacMaxRxAMPDUFactor, cD11HtMacMCSFeedbackImplemented=cD11HtMacMCSFeedbackImplemented, cD11HtMacPSMPControlledAccess=cD11HtMacPSMPControlledAccess, cD11HtMacDualCTSProtection=cD11HtMacDualCTSProtection, ciscoDot11HtMacMIBObjects=ciscoDot11HtMacMIBObjects, cD11HtMacPCOActivated=cD11HtMacPCOActivated, cD11HtMacMaxAMSDULength=cD11HtMacMaxAMSDULength)