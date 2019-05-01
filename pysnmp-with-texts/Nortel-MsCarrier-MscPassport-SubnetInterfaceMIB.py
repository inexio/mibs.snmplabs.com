#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:31:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
mscMod, mscModIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscMod", "mscModIndex")
DisplayString, RowStatus, StorageType, Unsigned32, Integer32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "DisplayString", "RowStatus", "StorageType", "Unsigned32", "Integer32")
DigitString, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "DigitString", "NonReplicated")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, IpAddress, ObjectIdentity, Bits, iso, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "ObjectIdentity", "Bits", "iso", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
subnetInterfaceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45))
mscModVcs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2))
mscModVcsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1), )
if mibBuilder.loadTexts: mscModVcsRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsRowStatusTable.setDescription('This entry controls the addition and deletion of mscModVcs components.')
mscModVcsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"))
if mibBuilder.loadTexts: mscModVcsRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsRowStatusEntry.setDescription('A single entry in the table represents a single mscModVcs component.')
mscModVcsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscModVcs components. These components can be added and deleted.')
mscModVcsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscModVcsComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscModVcsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscModVcsStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsStorageType.setDescription('This variable represents the storage type value for the mscModVcs tables.')
mscModVcsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscModVcsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsIndex.setDescription('This variable represents the index for the mscModVcs tables.')
mscModVcsAccOptTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10), )
if mibBuilder.loadTexts: mscModVcsAccOptTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsAccOptTable.setDescription("Accounting information is owned by the Vc System; it is stored in the Vc Accounting component, which itself is considered to be a component on the switch. The Accounting Component contains a bit map indicating which of the accounting facilities are to be spooled in the accounting record - for example, bit '0' if set indicates that the accounting facility with facility code H.00 should be spooled if present in the Vc for accounting purposes. The data contained in the Vc Accounting must be identical network wide even though the component can be changed and upgraded on a module by module basis.")
mscModVcsAccOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"))
if mibBuilder.loadTexts: mscModVcsAccOptEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsAccOptEntry.setDescription('An entry in the mscModVcsAccOptTable.')
mscModVcsSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("n1", 0), ("n2", 1), ("n4", 2), ("n8", 3), ("n16", 4), ("n32", 5), ("n64", 6), ("n128", 7), ("n256", 8), ("n512", 9), ("n1024", 10), ("n2048", 11), ("n4096", 12))).clone('n128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsSegmentSize.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsSegmentSize.setDescription('This attribute specifies the segment size for accounting of national calls. Minimum allowed segment size is 1. If data segment is sent which is less than segmentSize it is still counted as one segment.')
mscModVcsUnitsCounted = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("segments", 0), ("frames", 1))).clone('segments')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsUnitsCounted.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsUnitsCounted.setDescription('This attribute specifies what is counted by frame services. If set to frames, frames are counted, else segments are counted.')
mscModVcsAccountingFax = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="20")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsAccountingFax.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsAccountingFax.setDescription('Each value corresponds to an accounting facility code, of which there are currently 10 facility codes defined with codes H.00 to H.09, and corresponding to the above 10 facilities. Each of the above facilities may or may not be present and stored in the Vc for accounting purposes, depending on the nature of the call. For example, only those Vcs where a NUI (Network User Identifier) is used for charging or identification purposes will have a NUI stored in the Vc. Description of bits: notused0(0) notused1(1) originalCalledAddressFax(2)')
mscModVcsGenerationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("bothEnds", 0), ("singleEnd", 1))).clone('singleEnd')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsGenerationMode.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsGenerationMode.setDescription('This attribute specifies part of the rules by which the network generates accounting records. If set to bothEnds, then both ends of the Vc generate accounting records. If set to singleEnd, then the charged end of the Vc generates accounting records. In single end generation mode, if the call does not clear gracefully, both ends of the Vc will generate accounting record.')
mscModVcsAddOptTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12), )
if mibBuilder.loadTexts: mscModVcsAddOptTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsAddOptTable.setDescription('The Vc AddressingOptions group describes the addressing parameters. It is currently owned by the Vc. Most of the data contained in the Vc AddressingOptions group is identical network wide even though the group can be changed and upgraded on a module by module basis.')
mscModVcsAddOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"))
if mibBuilder.loadTexts: mscModVcsAddOptEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsAddOptEntry.setDescription('An entry in the mscModVcsAddOptTable.')
mscModVcsDefaultNumberingPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("x121", 0), ("e164", 1))).clone('x121')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsDefaultNumberingPlan.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsDefaultNumberingPlan.setDescription('This attribute specifies the numbering plan used which determines the address format: X.121-- the international numbering plan for public packet switched data networks or E.164-- the international numbering plan for ISDN and PSTN. The default numbering plan does not need to be consistent across all of the nodes in the network.')
mscModVcsNetworkIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dnic", 0), ("inic", 1))).clone('dnic')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscModVcsNetworkIdType.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsNetworkIdType.setDescription('This attribute specifies whether the network uses a DNIC or INIC. It is used by X.75 Gateways to indicate whether in network the DNIC or INIC is used in various utilities. If it is DNIC it can be DNIC or DCC type. If it is INIC it can be 4 digits only.')
mscModVcsX121Type = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dnic", 0), ("dcc", 1))).clone('dnic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsX121Type.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsX121Type.setDescription('This attribute specifies whether DNIC mode or DCC mode is used in X.121 address of international calls. If DCC is specified, then the first 3 digits of each DNA must be the Network ID Code. If this attribute is changed all Dnas in the network must start with this code. Numbering plan is affected by the change.')
mscModVcsNetworkIdCode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 6), DigitString().subtype(subtypeSpec=ValueSizeConstraint(3, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsNetworkIdCode.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsNetworkIdCode.setDescription('This attribute specifies the DNIC (Data Network ID Code) of the network or DCC code.')
mscModVcsX121IntlAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disallowed", 0), ("allowed", 1))).clone('allowed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsX121IntlAddresses.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsX121IntlAddresses.setDescription('This attribute indicates if any DTE is allowed to signal international addresses.')
mscModVcsX121IntllPrefixDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 9)).clone(9)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsX121IntllPrefixDigit.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsX121IntllPrefixDigit.setDescription('This attribute indicates the prefix digit to be used for X.121 international calls. When this digit is provided the call will have full international address.')
mscModVcsX121MinAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsX121MinAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsX121MinAddressLength.setDescription('This attribute indicates minimum length of x121 address.')
mscModVcsX121MaxAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsX121MaxAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsX121MaxAddressLength.setDescription('This attribute indicates maximum length of x121 address.')
mscModVcsX121ToE164EscapeSignificance = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsX121ToE164EscapeSignificance.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsX121ToE164EscapeSignificance.setDescription('This attribute specifies whether an X.121 to E.164 escape digit has significance in selecting an X.32 (analog) or an ISDN switched path. If two values are significant (the value 0 or the value 9) then yes is set to this attribute. If the value of the originally entered escape digit is not significant in routing the call then value of no is assigned to this attribute.')
mscModVcsE164IntlFormatAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disallowed", 0), ("allowed", 1))).clone('allowed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164IntlFormatAllowed.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164IntlFormatAllowed.setDescription("This attribute indicates whether or not to allow national format E.164 addresses. If this attribute is set to a value of Yes (=1) then national format E.164 addresses are not allowed and international format addresses only are allowed. If this attribute is set to a value of No (=0), then national format E.164 addresses are allowed. If only international format E.164 addresses are allowed, then the 'e164NatlPrefixDigit' attribute is not required, nor is the 'e164IntlPrefixDigits' required.")
mscModVcsE164IntlPrefixDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 15), DigitString().subtype(subtypeSpec=ValueSizeConstraint(0, 3)).clone(hexValue="30")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164IntlPrefixDigits.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164IntlPrefixDigits.setDescription("This attribute specifies the E.164 international prefix digits. If applicable, it is specified as 1 to 3 BCD digits. The 3 BCD digits are stored with the length of the international prefix in the low order nibble, nibble [0] followed by the most significant digit of the international prefix in the next low order nibble, nibble [1], etc. This attribute is not required if the corresponding attribute, 'e164IntlFormatOnly' is set to a value of Yes (=1).")
mscModVcsE164NatlPrefixDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 9)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164NatlPrefixDigit.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164NatlPrefixDigit.setDescription('This attribute contains the E.164 national prefix which may be added in front of E.164 local or national call. If e164IntlFormatOnly is set to 1, this attribute is not needed.')
mscModVcsE164LocalAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 15)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164LocalAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164LocalAddressLength.setDescription('This attribute indicates the length of a local E.164 DNA on this module. This attribute is not required if the corresponding attribute, e164IntlFormatOnly is set to a value of yes. This attribute does not need to be consistent across all of the nodes in the network.')
mscModVcsE164TeleCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 18), DigitString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone(hexValue="31")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164TeleCountryCode.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164TeleCountryCode.setDescription('This attribute specifies the E.164 Telephone Country Code (TCC) for the country in which the network resides. If applicable, it is specified as 1 to 3 BCD digits. The 3 BCD digits are stored with the length of the TCC in the low order nibble, nibble [0] followed by the most significant digit of the TCC in the next low order nibble, nibble [1], etc.')
mscModVcsE164NatlMinAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164NatlMinAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164NatlMinAddressLength.setDescription('This attribute indicates minimum length of e164 national address.')
mscModVcsE164NatlMaxAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164NatlMaxAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164NatlMaxAddressLength.setDescription('This attribute indicates maximum length of e164 national address.')
mscModVcsE164IntlMinAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164IntlMinAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164IntlMinAddressLength.setDescription('This attribute indicates minimum length of e164 international address.')
mscModVcsE164IntlMaxAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164IntlMaxAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164IntlMaxAddressLength.setDescription('This attribute indicates maximum length of e164 international address.')
mscModVcsE164LocalMinAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 24), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164LocalMinAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164LocalMinAddressLength.setDescription('This attribute indicates minimum length of e164 local address.')
mscModVcsE164LocalMaxAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 12, 1, 25), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsE164LocalMaxAddressLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsE164LocalMaxAddressLength.setDescription('This attribute indicates maximum length of e164 local address.')
mscModVcsIntOptTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13), )
if mibBuilder.loadTexts: mscModVcsIntOptTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsIntOptTable.setDescription('The Vc InterfaceOptions group defines Vc system parameters common in the network. It is owned by the Vc and is considered to be a module wide component on the switch. The data contained in the Vc InterfaceOptions group must be identical network wide even though this group can be changed and upgraded on a module by module basis.')
mscModVcsIntOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"))
if mibBuilder.loadTexts: mscModVcsIntOptEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsIntOptEntry.setDescription('An entry in the mscModVcsIntOptTable.')
mscModVcsHighPriorityPacketSizes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2).clone(hexValue="ff80")).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscModVcsHighPriorityPacketSizes.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsHighPriorityPacketSizes.setDescription('This attribute indicates which packet sizes are supported for high priority calls within the network. Description of bits: n16(0) n32(1) n64(2) n128(3) n256(4) n512(5) n1024(6) n2048(7) n4096(8)')
mscModVcsMaxSubnetPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("n16", 4), ("n32", 5), ("n64", 6), ("n128", 7), ("n256", 8), ("n512", 9), ("n1024", 10), ("n2048", 11), ("n4096", 12))).clone('n512')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsMaxSubnetPacketSize.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsMaxSubnetPacketSize.setDescription('This attribute specifies the maximum subnet packet size used for the connections originating or terminating on this module. All modules in the same network should have the same maxSubnetPacketSize. If this value is not identical throughout the network, the following points need to be considered: a) When Passport and DPN switches are connected in the same network, the maxSubnetPacketSize on a DPN switch can be at most 2048 and the DPN part of the network must be configured with hardware which supports this size: - Dedicated PE386 Network link/Trunk - Minimum measured link speed of 256Kbits/sec This hardware has to be present on every potential data path between connecting end points! b) The calling end of the connection signals the maxSubnetPacketSize value to the called end. The called end then compares this value to its own provisioned value and selects the smaller value. Note that this smaller value is not signalled back to the calling end. The calling and called ends can therefore have different maxSubnetPacketSize values.')
mscModVcsCallSetupTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsCallSetupTimer.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsCallSetupTimer.setDescription('This attribute specifies the Vc callSetupTimer in units of 1 second ticks. This timer specifies how long the Vc will wait, after sending a subnet Call Request packet into the network, for a response from the remote end of the Vc (in the form of a subnet Raccept packet). If, after sending a subnet Call packet into the network, a response is not received within this time period, the Vc will time out, clearing the call in the assumption that the remote end is unreachable. This timer must be long enough to take into account the time required for routing the subnet Call Request through the Source Call Routing and the Destination Call Routing systems in order to be delivered to the final destination.')
mscModVcsCallRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 300)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsCallRetryTimer.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsCallRetryTimer.setDescription('This attribute specifies, for Vc implementing Direct Calls with the auto-call retry feature (including PVCs), the Vc callRetryTimer in units of 1 second ticks. This timer specifies how long the Vc will wait between unsuccessful call attempts.')
mscModVcsDelaySubnetAcks = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsDelaySubnetAcks.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsDelaySubnetAcks.setDescription('This attribute specifies delay acknowledgment timer mechanism. If this attribute is set to no, then the Vc will automatically return acknowledgment packets without delay. If this attribute is set to yes, then the Vc will wait for one second in an attempt to piggyback the acknowledgment packet on another credit or data packet. If the Vc cannot piggyback the acknowledgment packet within this time, then the packet is returned without piggybacking.')
mscModVcsWinsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213), )
if mibBuilder.loadTexts: mscModVcsWinsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsWinsTable.setDescription('This is the windowSize corresponding to the given packet size and throughput class. All Vcs using the windowSize matrix support large Vc windows on both ends of the Vc, and support the signalling of the chosen Vc window size from the destination (called) end to the source (calling) end. This is the only matrix supported. The windowSize should be configured in the same way network wide, though it can be upgraded on a module by module basis. Vcs using the windowSize matrix will run properly if the matrices on different nodes differ since the Vc window is selected by the destination (called) side of the Vc.')
mscModVcsWinsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsWinsPktIndex"), (0, "Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", "mscModVcsWinsTptIndex"))
if mibBuilder.loadTexts: mscModVcsWinsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsWinsEntry.setDescription('An entry in the mscModVcsWinsTable.')
mscModVcsWinsPktIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("n16", 0), ("n32", 1), ("n64", 2), ("n128", 3), ("n256", 4), ("n512", 5), ("n1024", 6), ("n2048", 7), ("n4096", 8), ("n8192", 9), ("n32768", 10), ("n65535", 11))))
if mibBuilder.loadTexts: mscModVcsWinsPktIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsWinsPktIndex.setDescription('This variable represents the next to last index for the mscModVcsWinsTable.')
mscModVcsWinsTptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: mscModVcsWinsTptIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsWinsTptIndex.setDescription('This variable represents the final index for the mscModVcsWinsTable.')
mscModVcsWinsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 2, 213, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscModVcsWinsValue.setStatus('mandatory')
if mibBuilder.loadTexts: mscModVcsWinsValue.setDescription('This variable represents an individual value for the mscModVcsWinsTable.')
subnetInterfaceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1))
subnetInterfaceGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1, 1))
subnetInterfaceGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1, 1, 3))
subnetInterfaceGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 1, 1, 3, 2))
subnetInterfaceCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3))
subnetInterfaceCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3, 1))
subnetInterfaceCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3, 1, 3))
subnetInterfaceCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 45, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-SubnetInterfaceMIB", mscModVcsStorageType=mscModVcsStorageType, mscModVcs=mscModVcs, mscModVcsRowStatusEntry=mscModVcsRowStatusEntry, mscModVcsX121MinAddressLength=mscModVcsX121MinAddressLength, mscModVcsRowStatus=mscModVcsRowStatus, mscModVcsE164NatlMinAddressLength=mscModVcsE164NatlMinAddressLength, mscModVcsAccOptTable=mscModVcsAccOptTable, mscModVcsE164LocalAddressLength=mscModVcsE164LocalAddressLength, mscModVcsE164IntlMinAddressLength=mscModVcsE164IntlMinAddressLength, mscModVcsE164IntlMaxAddressLength=mscModVcsE164IntlMaxAddressLength, mscModVcsE164LocalMaxAddressLength=mscModVcsE164LocalMaxAddressLength, mscModVcsWinsTptIndex=mscModVcsWinsTptIndex, mscModVcsE164IntlPrefixDigits=mscModVcsE164IntlPrefixDigits, mscModVcsComponentName=mscModVcsComponentName, mscModVcsIndex=mscModVcsIndex, subnetInterfaceGroupCA=subnetInterfaceGroupCA, mscModVcsX121IntllPrefixDigit=mscModVcsX121IntllPrefixDigit, mscModVcsDelaySubnetAcks=mscModVcsDelaySubnetAcks, mscModVcsX121Type=mscModVcsX121Type, mscModVcsWinsTable=mscModVcsWinsTable, mscModVcsE164NatlPrefixDigit=mscModVcsE164NatlPrefixDigit, subnetInterfaceMIB=subnetInterfaceMIB, mscModVcsAccountingFax=mscModVcsAccountingFax, mscModVcsMaxSubnetPacketSize=mscModVcsMaxSubnetPacketSize, mscModVcsAddOptTable=mscModVcsAddOptTable, mscModVcsWinsValue=mscModVcsWinsValue, subnetInterfaceCapabilitiesCA02A=subnetInterfaceCapabilitiesCA02A, subnetInterfaceCapabilities=subnetInterfaceCapabilities, subnetInterfaceGroupCA02=subnetInterfaceGroupCA02, subnetInterfaceCapabilitiesCA=subnetInterfaceCapabilitiesCA, mscModVcsX121MaxAddressLength=mscModVcsX121MaxAddressLength, mscModVcsE164IntlFormatAllowed=mscModVcsE164IntlFormatAllowed, subnetInterfaceGroup=subnetInterfaceGroup, mscModVcsSegmentSize=mscModVcsSegmentSize, mscModVcsX121IntlAddresses=mscModVcsX121IntlAddresses, mscModVcsGenerationMode=mscModVcsGenerationMode, mscModVcsWinsEntry=mscModVcsWinsEntry, mscModVcsUnitsCounted=mscModVcsUnitsCounted, mscModVcsNetworkIdType=mscModVcsNetworkIdType, mscModVcsAccOptEntry=mscModVcsAccOptEntry, mscModVcsAddOptEntry=mscModVcsAddOptEntry, mscModVcsX121ToE164EscapeSignificance=mscModVcsX121ToE164EscapeSignificance, mscModVcsDefaultNumberingPlan=mscModVcsDefaultNumberingPlan, mscModVcsIntOptTable=mscModVcsIntOptTable, mscModVcsCallRetryTimer=mscModVcsCallRetryTimer, mscModVcsWinsPktIndex=mscModVcsWinsPktIndex, mscModVcsCallSetupTimer=mscModVcsCallSetupTimer, mscModVcsE164NatlMaxAddressLength=mscModVcsE164NatlMaxAddressLength, subnetInterfaceGroupCA02A=subnetInterfaceGroupCA02A, mscModVcsNetworkIdCode=mscModVcsNetworkIdCode, mscModVcsE164TeleCountryCode=mscModVcsE164TeleCountryCode, mscModVcsIntOptEntry=mscModVcsIntOptEntry, subnetInterfaceCapabilitiesCA02=subnetInterfaceCapabilitiesCA02, mscModVcsE164LocalMinAddressLength=mscModVcsE164LocalMinAddressLength, mscModVcsRowStatusTable=mscModVcsRowStatusTable, mscModVcsHighPriorityPacketSizes=mscModVcsHighPriorityPacketSizes)
