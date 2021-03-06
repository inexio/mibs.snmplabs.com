#
# PySNMP MIB module RFC1304-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1304-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:56:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, transmission, TimeTicks, iso, Integer32, NotificationType, Counter32, Bits, Gauge32, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "transmission", "TimeTicks", "iso", "Integer32", "NotificationType", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sip = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 31))
class SMDSAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

sipL3Table = MibTable((1, 3, 6, 1, 2, 1, 10, 31, 1), )
if mibBuilder.loadTexts: sipL3Table.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3Table.setDescription('This table contains SIP L3 parameters and state variables, one entry per SIP port.')
sipL3Entry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 31, 1, 1), ).setIndexNames((0, "RFC1304-MIB", "sipL3Index"))
if mibBuilder.loadTexts: sipL3Entry.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3Entry.setDescription('This list contains SIP L3 parameters and state variables.')
sipL3Index = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3Index.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3Index.setDescription('The value of this object identifies the SIP port interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in RFC 1156 and RFC 1213, for the same interface.')
sipL3ReceivedIndividualDAs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3ReceivedIndividualDAs.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3ReceivedIndividualDAs.setDescription('The total number of individually addressed SIP Level 3 PDUs received from the remote system across the SNI. The total includes only unerrored L3PDUs.')
sipL3ReceivedGAs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3ReceivedGAs.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3ReceivedGAs.setDescription('The total number of group addressed SIP Level 3 PDUs received from the remote system across the SNI. The total includes only unerrored L3PDUs.')
sipL3UnrecognizedIndividualDAs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3UnrecognizedIndividualDAs.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3UnrecognizedIndividualDAs.setDescription('The number of SIP Level 3 PDUs received from the remote system with invalid or unknown individual destination addresses (Destination Address Screening violations are not included). See SMDS Subscription MIB module.')
sipL3UnrecognizedGAs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3UnrecognizedGAs.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3UnrecognizedGAs.setDescription('The number of SIP Level 3 PDUs received from the remote system with invalid or unknown group addresses. (Destination Address Screening violations are not included). See SMDS Subscription MIB module.')
sipL3SentIndividualDAs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3SentIndividualDAs.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3SentIndividualDAs.setDescription('The number of individually addressed SIP Level 3 PDUs that have been sent by this system across the SNI.')
sipL3SentGAs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3SentGAs.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3SentGAs.setDescription('The number of group addressed SIP L3PDUs that have been sent by this system across the SNI.')
sipL3Errors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3Errors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3Errors.setDescription('The total number of SIP Level 3 PDUs received from the remote system that were discovered to have errors (including protocol processing and bit errors but excluding addressing-related errors) and were discarded. Includes both group addressed L3PDUs and L3PDUs containing an individual destination address.')
sipL3InvalidSMDSAddressTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3InvalidSMDSAddressTypes.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3InvalidSMDSAddressTypes.setDescription('The number of SIP Level 3 PDUs received from the remote system that had the Source or Destination Address_Type subfields, (the four most significant bits of the 64 bit address field), not equal to the value 1100 or 1110. Also, an error is considered to have occurred if the Address_Type field for a Source Address, the four most significant bits of the 64 bits, is equal to 1110 (a group address).')
sipL3VersionSupport = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3VersionSupport.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3VersionSupport.setDescription('A value which indicates the version(s) of SIP that this interface supports. The value is a sum. This sum initially takes the value zero. For each version, V, that this interface supports, 2 raised to (V - 1) is added to the sum. For example, a port supporting versions 1 and 2 would have a value of (2^(1-1)+2^(2-1))=3. The sipL3VersionSupport is effectively a bit mask with Version 1 equal to the least significant bit (LSB).')
sipL2Table = MibTable((1, 3, 6, 1, 2, 1, 10, 31, 2), )
if mibBuilder.loadTexts: sipL2Table.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2Table.setDescription('This table contains SIP L2PDU parameters and state variables, one entry per SIP port.')
sipL2Entry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 31, 2, 1), ).setIndexNames((0, "RFC1304-MIB", "sipL2Index"))
if mibBuilder.loadTexts: sipL2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2Entry.setDescription('This list contains SIP L2 parameters and state variables.')
sipL2Index = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2Index.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2Index.setDescription('The value of this object identifies the SIP port interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in RFC 1156 and RFC 1213, for the same interface.')
sipL2ReceivedCounts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2ReceivedCounts.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2ReceivedCounts.setDescription('The number of SIP Level 2 PDUs received from the remote system across the SNI. The total includes only unerrored L2PDUs.')
sipL2SentCounts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2SentCounts.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2SentCounts.setDescription('The number of SIP Level 2 PDUs that have been sent by this system across the SNI.')
sipL2HcsOrCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2HcsOrCRCErrors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2HcsOrCRCErrors.setDescription('The number of received SIP Level 2 PDUs that were discovered to have either a Header Check Sequence error or a Payload CRC violation.')
sipL2PayloadLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2PayloadLengthErrors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2PayloadLengthErrors.setDescription('The number of received SIP Level 2 PDUs that had Payload Length errors that fall in the following specifications: - SSM L2_PDU payload length field value less - than 28 octets or greater than 44 octets, - BOM or COM L2_PDU payload length field not - equal to 44 octets, - EOM L2_PDU payload length field value less - than 4 octets or greater than 44 octets.')
sipL2SequenceNumberErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2SequenceNumberErrors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2SequenceNumberErrors.setDescription('The number of received SIP Level 2 PDUs that had a sequence number within the L2PDU not equal to the expected sequence number of the SMDS SS receive process.')
sipL2MidCurrentlyActiveErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2MidCurrentlyActiveErrors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2MidCurrentlyActiveErrors.setDescription('The number of received SIP Level 2 PDUs that are BOMs for which an active receive process is already started.')
sipL2BomOrSSMsMIDErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2BomOrSSMsMIDErrors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2BomOrSSMsMIDErrors.setDescription('The number of received SIP Level 2 PDUs that are SSMs with a MID not equal to zero or are BOMs with MIDs equal to zero.')
sipL2EomsMIDErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL2EomsMIDErrors.setStatus('mandatory')
if mibBuilder.loadTexts: sipL2EomsMIDErrors.setDescription('The number of received SIP Level 2 PDUs that are EOMs for which there is no active receive process for the MID (i.e., the receipt of an EOM which does not correspond to a BOM) OR the EOM has a MID equal to zero.')
sipPLCP = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 31, 3))
sipDS1PLCPTable = MibTable((1, 3, 6, 1, 2, 1, 10, 31, 3, 1), )
if mibBuilder.loadTexts: sipDS1PLCPTable.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS1PLCPTable.setDescription('This table contains SIP DS1 PLCP parameters and state variables, one entry per SIP port.')
sipDS1PLCPEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1), ).setIndexNames((0, "RFC1304-MIB", "sipDS1PLCPIndex"))
if mibBuilder.loadTexts: sipDS1PLCPEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS1PLCPEntry.setDescription('This list contains SIP DS1 PLCP parameters and state variables.')
sipDS1PLCPIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS1PLCPIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS1PLCPIndex.setDescription('The value of this object identifies the SIP port interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in RFC 1156 and RFC 1213, for the same interface.')
sipDS1PLCPSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS1PLCPSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS1PLCPSEFSs.setDescription('A DS1 Severely Errored Framing Second (SEFS) is a count of one-second intervals containing one or more SEF events. A Severely Errored Framing (SEF) event is declared when an error in the A1 octet and an error in the A2 octet of a framing octet pair (i.e., errors in both framing octets), or two consecutive invalid and/or nonsequential Path Overhead Identifier octets are detected.')
sipDS1PLCPAlarmState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAlarm", 1), ("receivedFarEndAlarm", 2), ("incomingLOF", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS1PLCPAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS1PLCPAlarmState.setDescription('This variable indicates if there is an alarm present for the DS1 PLCP. The value receivedFarEndAlarm means that the DS1 PLCP has received an incoming Yellow Signal, the value incomingLOF means that the DS1 PLCP has declared a loss of frame (LOF) failure condition, and the value noAlarm means that there are no alarms present. See TR-TSV-000773 for a description of alarm states.')
sipDS1PLCPUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS1PLCPUASs.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS1PLCPUASs.setDescription('The counter associated with the number of Unavailable Seconds, as defined by TR-TSV-000773, encountered by the PLCP.')
sipDS3PLCPTable = MibTable((1, 3, 6, 1, 2, 1, 10, 31, 3, 2), )
if mibBuilder.loadTexts: sipDS3PLCPTable.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS3PLCPTable.setDescription('This table contains SIP DS3 PLCP parameters and state variables, one entry per SIP port.')
sipDS3PLCPEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1), ).setIndexNames((0, "RFC1304-MIB", "sipDS3PLCPIndex"))
if mibBuilder.loadTexts: sipDS3PLCPEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS3PLCPEntry.setDescription('This list contains SIP DS3 PLCP parameters and state variables.')
sipDS3PLCPIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS3PLCPIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS3PLCPIndex.setDescription('The value of this object identifies the SIP port interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in RFC 1156 and RFC 1213, for the same interface.')
sipDS3PLCPSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS3PLCPSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS3PLCPSEFSs.setDescription('A DS3 Severely Errored Framing Second (SEFS) is a count of one-second intervals containing one or more SEF events. A Severely Errored Framing (SEF) event is declared when an error in the A1 octet and an error in the A2 octet of a framing octet pair (i.e., errors in both framing octets), or two consecutive invalid and/or nonsequential Path Overhead Identifier octets are detected.')
sipDS3PLCPAlarmState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAlarm", 1), ("receivedFarEndAlarm", 2), ("incomingLOF", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS3PLCPAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS3PLCPAlarmState.setDescription('This variable indicates if there is an alarm present for the DS3 PLCP. The value receivedFarEndAlarm means that the DS3 PLCP has received an incoming Yellow Signal, the value incomingLOF means that the DS3 PLCP has declared a loss of frame (LOF) failure condition, and the value noAlarm means that there are no alarms present. See TR-TSV-000773 for a description of alarm states.')
sipDS3PLCPUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipDS3PLCPUASs.setStatus('mandatory')
if mibBuilder.loadTexts: sipDS3PLCPUASs.setDescription('The counter associated with the number of Unavailable Seconds, as defined by TR-TSV-000773, encountered by the PLCP.')
smdsApplications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 31, 4))
ipOverSMDS = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 31, 4, 1))
ipOverSMDSTable = MibTable((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1), )
if mibBuilder.loadTexts: ipOverSMDSTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSTable.setDescription("The table of addressing information relevant to this entity's IP addresses.")
ipOverSMDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1), ).setIndexNames((0, "RFC1304-MIB", "ipOverSMDSIndex"), (0, "RFC1304-MIB", "ipOverSMDSAddress"))
if mibBuilder.loadTexts: ipOverSMDSEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSEntry.setDescription("The addressing information for one of this entity's IP addresses.")
ipOverSMDSIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOverSMDSIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSIndex.setDescription('The value of this object identifies the SIP port interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in RFC 1156 and RFC 1213, for the same interface.')
ipOverSMDSAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOverSMDSAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSAddress.setDescription("The IP address to which this entry's addressing information pertains.")
ipOverSMDSHA = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 3), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOverSMDSHA.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSHA.setDescription('The SMDS Individual address of the IP station.')
ipOverSMDSLISGA = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 4), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOverSMDSLISGA.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSLISGA.setDescription('The SMDS Group Address that has been configured to identify the SMDS Subscriber-Network Interfaces (SNIs) of all members of the Logical IP Subnetwork (LIS) connected to the network supporting SMDS.')
ipOverSMDSARPReq = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 4, 1, 1, 1, 5), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOverSMDSARPReq.setStatus('mandatory')
if mibBuilder.loadTexts: ipOverSMDSARPReq.setDescription('The SMDS address (individual or group) to which ARP Requests are to be sent.')
smdsCarrierSelection = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 31, 5))
sipErrorLog = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 31, 6))
sipL3PDUErrorTable = MibTable((1, 3, 6, 1, 2, 1, 10, 31, 6, 1), )
if mibBuilder.loadTexts: sipL3PDUErrorTable.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorTable.setDescription("A table that contains the latest occurrence of the following syntactical SIP L3PDU errors: - Destination Address Field Format Error, The following pertains to the 60 least significant bits of the 64 bit address field. The 60 bits contained in the address subfield can be used to represent addresses up to 15 decimal digits. Each decimal digit shall be encoded into four bits using Binary Coded Decimal (BCD), with the most significant digit occurring left-most. If not all 15 digits are required, then the remainder of this field shall be padded on the right with bits set to one. An error is considered to have occurred: a). if the first four bits of the address subfield are not BCD, OR b). if the first four bits of the address subfield are populated with the country code value 0001, AND the 40 bits which follow are not Binary Coded Decimal (BCD) encoded values of the 10 digit addresses, OR the remaining 16 least significant bits are not populated with 1's, OR c). if the address subfield is not correct according to another numbering plan which is dependent upon the carrier assigning the numbers and offering SMDS. - Source Address Field Format Error, The description of this parameter is the same as the description of the Destination Address Field Format Error. - Invalid BAsize Field Value, An error is considered to have occurred when the BAsize field of an SIP L3PDU contains a value less that 32, greater than 9220 octets without the CRC32 field present, greater than 9224 octets with the CRC32 field present, or not equal to a multiple of 4 octets, - Invalid Header Extension Length Field Value, An error is considered to have occurred when the Header Extension Length field value is not equal 3. - Invalid Header Extension - Element Length, An error is considered to have occurred when the Header Extension - Element Length is greater than 12. - Invalid Header Extension - Version Element Position, Length, or Value, An error is considered to have occurred when a Version element with Length=3, Type=0, and Value=1 does not appear first within the Header Extension, or an element Type=0 appears somewhere other than within the first three octets in the Header Extension. - Invalid Header Extension - Carrier Selection Element Position, Length, Value or Format, An error is considered to have occurred when a Carrier Selection element does not appear second within the Header Extension, if the Element Type does not equal 1, the Element Length does not equal 4, 6, or 8, the Element Value field is not four BCD encoded decimal digits used in specifying the Carrier Identification Code (CIC), or the identified CIC code is invalid. - Header Extension PAD Error An error is considered to have occurred when the Header Extension PAD is 9 octets in length, or if the Header Extension PAD is greater than zero octets in length and the Header Extension PAD does not follow all Header Extension elements or does not begin with at least one octet of all zeros. - BEtag Mismatch Error, An error is considered to have occurred when the Beginning-End Tags in the SIP L3PDU header and trailer are not equal. - BAsize Field not equal to Length Field Error, An error is considered to have occurred when the value of the BAsize Field does not equal the value of the Length Field. - Incorrect Length Error, and An error is considered to have occurred when the the Length field value is not equal to the portion of the SIP L3PDU which extends from the Destination Address field up to and including the CRC32 field (if present) or up to and including the PAD field (if the CRC32 field is not present). As an optional check, an error is considered to have occurred when the length of a partially received SIP L3PDU exceeds the BAsize value. - MRI Timeout Error. An error is considered to have occurred when the elapsed time between receipt of BOM and corresponding EOM exceeds the value of the MRI (Message Receive Interval) for a particular transport signal format. An entry is indexed by interface number and error type, and contains Source Address, Destination Address and a timestamp. All these errors are counted in the sipL3Errors counter. When sipL3PDUErrorTimeStamp is equal to zero, the SipL3PDUErrorEntry does not contain any valid information.")
sipL3PDUErrorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1), ).setIndexNames((0, "RFC1304-MIB", "sipL3PDUErrorIndex"), (0, "RFC1304-MIB", "sipL3PDUErrorType"))
if mibBuilder.loadTexts: sipL3PDUErrorEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorEntry.setDescription('An entry in the service disagreement table.')
sipL3PDUErrorIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3PDUErrorIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorIndex.setDescription('The value of this object identifies the SIP port interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in RFC 1156 and RFC 1213, for the same interface.')
sipL3PDUErrorType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("erroredDAFieldFormat", 1), ("erroredSAFieldFormat", 2), ("invalidBAsizeFieldValue", 3), ("invalidHdrExtLength", 4), ("invalidHdrExtElementLength", 5), ("invalidHdrExtVersionElementPositionLenthOrValue", 6), ("invalidHdrExtCarSelectElementPositionLenghtValueOrFormat", 7), ("hePADError", 8), ("beTagMismatch", 9), ("baSizeFieldNotEqualToLengthField", 10), ("incorrectLength", 11), ("mriTimeout", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3PDUErrorType.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorType.setDescription('The type of error.')
sipL3PDUErrorSA = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 3), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3PDUErrorSA.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorSA.setDescription('A rejected SMDS source address.')
sipL3PDUErrorDA = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 4), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3PDUErrorDA.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorDA.setDescription('A rejected SMDS destination address.')
sipL3PDUErrorTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 31, 6, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipL3PDUErrorTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: sipL3PDUErrorTimeStamp.setDescription('The timestamp for the service disagreement. The timestamp contains the value of sysUpTime at the latest occurrence of this type of service disagreement. See textual description under sipL3PDUErrorTable for boundary conditions.')
mibBuilder.exportSymbols("RFC1304-MIB", sipL3SentGAs=sipL3SentGAs, sipL2Table=sipL2Table, ipOverSMDSLISGA=ipOverSMDSLISGA, sipL2SequenceNumberErrors=sipL2SequenceNumberErrors, sipL2SentCounts=sipL2SentCounts, sipL3PDUErrorTimeStamp=sipL3PDUErrorTimeStamp, ipOverSMDSARPReq=ipOverSMDSARPReq, sip=sip, sipL2Index=sipL2Index, sipL2ReceivedCounts=sipL2ReceivedCounts, sipDS1PLCPAlarmState=sipDS1PLCPAlarmState, sipL2MidCurrentlyActiveErrors=sipL2MidCurrentlyActiveErrors, sipL3PDUErrorEntry=sipL3PDUErrorEntry, ipOverSMDSTable=ipOverSMDSTable, ipOverSMDSAddress=ipOverSMDSAddress, sipL2BomOrSSMsMIDErrors=sipL2BomOrSSMsMIDErrors, sipDS3PLCPEntry=sipDS3PLCPEntry, sipL2EomsMIDErrors=sipL2EomsMIDErrors, sipDS3PLCPIndex=sipDS3PLCPIndex, sipL3PDUErrorTable=sipL3PDUErrorTable, sipL3Entry=sipL3Entry, sipL2Entry=sipL2Entry, SMDSAddress=SMDSAddress, sipL2HcsOrCRCErrors=sipL2HcsOrCRCErrors, ipOverSMDS=ipOverSMDS, sipDS3PLCPUASs=sipDS3PLCPUASs, sipL3Errors=sipL3Errors, sipPLCP=sipPLCP, sipL3Index=sipL3Index, sipL3ReceivedGAs=sipL3ReceivedGAs, sipDS1PLCPIndex=sipDS1PLCPIndex, sipDS1PLCPUASs=sipDS1PLCPUASs, sipL3PDUErrorType=sipL3PDUErrorType, sipDS1PLCPSEFSs=sipDS1PLCPSEFSs, ipOverSMDSHA=ipOverSMDSHA, sipL3PDUErrorDA=sipL3PDUErrorDA, smdsApplications=smdsApplications, sipDS1PLCPTable=sipDS1PLCPTable, ipOverSMDSEntry=ipOverSMDSEntry, sipL3VersionSupport=sipL3VersionSupport, sipL3PDUErrorSA=sipL3PDUErrorSA, sipL3ReceivedIndividualDAs=sipL3ReceivedIndividualDAs, sipL2PayloadLengthErrors=sipL2PayloadLengthErrors, sipErrorLog=sipErrorLog, ipOverSMDSIndex=ipOverSMDSIndex, sipL3PDUErrorIndex=sipL3PDUErrorIndex, sipDS1PLCPEntry=sipDS1PLCPEntry, sipDS3PLCPTable=sipDS3PLCPTable, sipDS3PLCPAlarmState=sipDS3PLCPAlarmState, smdsCarrierSelection=smdsCarrierSelection, sipL3UnrecognizedGAs=sipL3UnrecognizedGAs, sipL3UnrecognizedIndividualDAs=sipL3UnrecognizedIndividualDAs, sipL3InvalidSMDSAddressTypes=sipL3InvalidSMDSAddressTypes, sipL3SentIndividualDAs=sipL3SentIndividualDAs, sipDS3PLCPSEFSs=sipDS3PLCPSEFSs, sipL3Table=sipL3Table)
