#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-HuntGroupMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-HuntGroupMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:30:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
StorageType, Counter32, DisplayString, Unsigned32, RowStatus, Integer32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "Counter32", "DisplayString", "Unsigned32", "RowStatus", "Integer32")
Link, AsciiString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link", "AsciiString")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, IpAddress, Unsigned32, MibIdentifier, Bits, Counter64, ModuleIdentity, Integer32, Gauge32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "IpAddress", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
huntGroupMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130))
mscHg = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131))
mscHgRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1), )
if mibBuilder.loadTexts: mscHgRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgRowStatusTable.setDescription('This entry controls the addition and deletion of mscHg components.')
mscHgRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgRowStatusEntry.setDescription('A single entry in the table represents a single mscHg component.')
mscHgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscHg components. These components can be added and deleted.')
mscHgComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscHgStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgStorageType.setDescription('This variable represents the storage type value for the mscHg tables.')
mscHgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: mscHgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgIndex.setDescription('This variable represents the index for the mscHg tables.')
mscHgCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10), )
if mibBuilder.loadTexts: mscHgCidDataTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgCidDataTable.setDescription("This group contains the attribute for a component's Customer Identifier (CID). Refer to the attribute description for a detailed explanation of CIDs.")
mscHgCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgCidDataEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgCidDataEntry.setDescription('An entry in the mscHgCidDataTable.')
mscHgCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgCustomerIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgCustomerIdentifier.setDescription("This attribute holds the Customer Identifier (CID). Every component has a CID. If a component has a cid attribute, the component's CID is the provisioned value of that attribute; otherwise the component inherits the CID of its parent. The top- level component has a CID of 0. Every operator session also has a CID, which is the CID provisioned for the operator's user ID. An operator will see only the stream data for components having a matching CID. Also, the operator will be allowed to issue commands for only those components which have a matching CID. An operator CID of 0 is used to identify the Network Manager (referred to as 'NetMan' in DPN). This CID matches the CID of any component. Values 1 to 8191 inclusive (equivalent to 'basic CIDs' in DPN) may be assigned to specific customers.")
mscHgNsapAddressTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11), )
if mibBuilder.loadTexts: mscHgNsapAddressTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgNsapAddressTable.setDescription('This group contains attributes common to all NSAP format addresses.')
mscHgNsapAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgNsapAddressEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgNsapAddressEntry.setDescription('An entry in the mscHgNsapAddressTable.')
mscHgAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgAddress.setDescription('The address attribute specifies the numbering plan and digits which form a unique DNA identifier of the hunt group. The format of the address attribute is <numberingPlan>.<digits> where numbering plan is x for X.121 and e for E.164. An example X.121 address is x.12345678.')
mscHgProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12), )
if mibBuilder.loadTexts: mscHgProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgProvTable.setDescription('The Provisioned group contains the provisioned attributes of the hunt group.')
mscHgProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgProvEntry.setDescription('An entry in the mscHgProvTable.')
mscHgLogicalProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgLogicalProcessor.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgLogicalProcessor.setDescription('This attribute specifies the logical processor on which the hunt group process will execute. The Lp/n Eng Hgs component contains statistics for all hunt groups on the LP.')
mscHgSelectionPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("startFromZero", 0), ("rotary", 1), ("mostAvailable", 2))).clone('mostAvailable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgSelectionPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgSelectionPolicy.setDescription('The selectionPolicy attribute specifies the algorithm used to select a hunt group member. A value of startFromZero means that on a new call, the first available member starting from the member with the lowest instance value is selected. Subsequent hunts for the same call select the first available member starting from the previously chosen member. This algorithm is used when it is desirable to have the first member receive the majority of the calls and subsequent members only receive calls in overflow situations. A value of rotary means that on a new call, the first available member is selected starting from the member which received the last new call. Subsequent hunts for the same call select the first available member starting from the previously chosen member. This algorithm is used when it is desirable to loadspread the calls equally across the members. A value of mostAvailable means that on a new call, the most available member is selected based on the availability information received from the member. Subsequent hunts for the same call select the most available member starting from the previously chosen member. This algorithm is used when it is desirable to send each call to the member which has the highest probability of connecting it.')
mscHgMaxHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)).clone(63)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgMaxHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgMaxHuntAttempts.setDescription('The maxHuntAttempts attribute specifies the maximum attempts allowed to hunt the call. Hunting ceases if either this maximum is exceeded or the member list is exhausted.')
mscHgAppendSuffixDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgAppendSuffixDigits.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgAppendSuffixDigits.setDescription('The appendSuffixDigits attribute specifies how suffix called address digits are handled. Suffix called address digits are any trailing digits, signalled in a call, beyond the provisioned hunt group address. If this attribute is set to yes, suffix digits are appended to the member address before the call is forwarded to the member. If it is set to no, suffix digits are not appended to the member address.')
mscHgStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20), )
if mibBuilder.loadTexts: mscHgStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscHgStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgStateEntry.setDescription('An entry in the mscHgStateTable.')
mscHgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscHgOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscHgUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscHgOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21), )
if mibBuilder.loadTexts: mscHgOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgOperationalTable.setDescription('The Operational group contains the operational attributes of the hunt group.')
mscHgOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgOperationalEntry.setDescription('An entry in the mscHgOperationalTable.')
mscHgHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHuntAttempts.setDescription('This attribute counts the total number of hunt attempts made by the hunt group. The count includes both initial and subsequent hunt attempts. This count is contained within the huntAttempts attribute of the Lp/n Eng Hgs component. This counter wraps to 0 when it exceeds its maximum value.')
mscHgFailedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgFailedCalls.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgFailedCalls.setDescription('This attribute counts the number of calls which could not be connected by any of the hunt group members. This could occur if the hunt group is locked or has exhausted its member list. If a call cannot be connected by the hunt group it is sent to call redirection. This counter wraps to 0 when it exceeds its maximum value.')
mscHgInitialHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgInitialHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgInitialHuntAttempts.setDescription('This attribute counts the number of new (non-hunted) calls received by the hunt group which are forwarded to a member. This counter wraps to 0 when it exceeds its maximum value.')
mscHgAvailabilityUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgAvailabilityUpdates.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgAvailabilityUpdates.setDescription('This attribute counts the number of availability update packets received by the hunt group from its members. This counter wraps to 0 when it exceeds its maximum value.')
mscHgMaxAddrLenExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgMaxAddrLenExceeded.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgMaxAddrLenExceeded.setDescription('This attribute counts the number of times a member could not be selected to receive a call with suffix address digits because its DNA length would exceed the maximum of 14 digits with the suffix digits appended. This counter wraps to 0 when it exceeds its maximum value.')
mscHgBadPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgBadPackets.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgBadPackets.setDescription('This attribute counts the number of unrecognizable packets received by the hunt group and discarded. This counter wraps to 0 when it exceeds its maximum value.')
mscHgHgM = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2))
mscHgHgMRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1), )
if mibBuilder.loadTexts: mscHgHgMRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMRowStatusTable.setDescription('This entry controls the addition and deletion of mscHgHgM components.')
mscHgHgMRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMRowStatusEntry.setDescription('A single entry in the table represents a single mscHgHgM component.')
mscHgHgMRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgHgMRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscHgHgM components. These components can be added and deleted.')
mscHgHgMComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscHgHgMStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMStorageType.setDescription('This variable represents the storage type value for the mscHgHgM tables.')
mscHgHgMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)))
if mibBuilder.loadTexts: mscHgHgMIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMIndex.setDescription('This variable represents the index for the mscHgHgM tables.')
mscHgHgMProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10), )
if mibBuilder.loadTexts: mscHgHgMProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMProvTable.setDescription('The Provisioned group contains the provisioned attributes of the hunt group member.')
mscHgHgMProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMProvEntry.setDescription('An entry in the mscHgHgMProvTable.')
mscHgHgMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgHgMAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMAddress.setDescription('The address attribute specifies the numbering plan and digits which form a unique DNA identifier of the hunt group member. The format of the address attribute is <numberingPlan>.<digits> where numbering plan is x for X.121 and e for E.164. An example X.121 address is x.12345678.')
mscHgHgMStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11), )
if mibBuilder.loadTexts: mscHgHgMStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscHgHgMStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMStateEntry.setDescription('An entry in the mscHgHgMStateTable.')
mscHgHgMAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscHgHgMOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscHgHgMUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscHgHgMOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12), )
if mibBuilder.loadTexts: mscHgHgMOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMOperationalTable.setDescription('The Operational group defines operational attributes associated with the HuntGroupMember component.')
mscHgHgMOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMOperationalEntry.setDescription('An entry in the mscHgHgMOperationalTable.')
mscHgHgMAvailability = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)).clone(4095)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgHgMAvailability.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMAvailability.setDescription("This attribute indicates the current availability of the member. The higher the value, the more available the member is perceived to be. A value of 0 indicates the member is unavailable. A member must be considered 'available' by the hunt group in order to receive a call, regardless of the selection policy in use. The hunt group members report whether or not they are available to receive calls to the hunt group. Some services base their availability on unused logical channels, others on bandwidth or memory capacity. During initialization, the hunt group assumes all of its members are equally available and sets their availability value to the maximum of 4095. Similarly, a new hunt group member added to an existing hunt group has its availability value initialized to 4095. This ensures that members which have not reported their availability to the hunt group are tried in order to trigger the member to report its true availability. The availability of a member can change in the following ways: - Hunt group members can report their availability to the hunt group using a DPRS availability packet. - A network operator can temporarily change the value by the Set command. This change remains in effect until changed again by any of these ways. - The hunt group resets a member's availability to the maximum of 4095 if it has been 0 for at least 2.5 hours. This ensures that 'lost' availability information does not prevent a member from returning to service.")
mscHgHgMAvailabilityUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMAvailabilityUpdates.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMAvailabilityUpdates.setDescription('This attribute counts the number of availability update packets received by the hunt group member. This counter wraps to 0 when it exceeds its maximum value.')
mscHgHgMCallsRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMCallsRefused.setStatus('mandatory')
if mibBuilder.loadTexts: mscHgHgMCallsRefused.setDescription("This attribute counts the number of call packets which were returned to the hunt group by the member because it could not connect the call. If this counter increments frequently, it could indicate a problem with the member's reporting of its availability to the hunt group or an incompatibility in the call options. This counter wraps to 0 when it exceeds its maximum value.")
huntGroupGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1))
huntGroupGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1))
huntGroupGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1, 3))
huntGroupGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1, 3, 2))
huntGroupCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3))
huntGroupCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1))
huntGroupCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1, 3))
huntGroupCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-HuntGroupMIB", huntGroupGroupCA02=huntGroupGroupCA02, mscHgLogicalProcessor=mscHgLogicalProcessor, mscHgStorageType=mscHgStorageType, mscHgCustomerIdentifier=mscHgCustomerIdentifier, mscHgOperationalState=mscHgOperationalState, mscHgIndex=mscHgIndex, huntGroupCapabilitiesCA02A=huntGroupCapabilitiesCA02A, mscHgHgMCallsRefused=mscHgHgMCallsRefused, huntGroupCapabilitiesCA=huntGroupCapabilitiesCA, mscHgMaxAddrLenExceeded=mscHgMaxAddrLenExceeded, mscHgComponentName=mscHgComponentName, mscHgHgMAddress=mscHgHgMAddress, mscHgNsapAddressTable=mscHgNsapAddressTable, mscHgHgMUsageState=mscHgHgMUsageState, mscHgHgMOperationalEntry=mscHgHgMOperationalEntry, mscHgHgM=mscHgHgM, mscHgHgMRowStatus=mscHgHgMRowStatus, mscHgHgMStateTable=mscHgHgMStateTable, mscHgHgMStateEntry=mscHgHgMStateEntry, mscHg=mscHg, mscHgHgMComponentName=mscHgHgMComponentName, mscHgRowStatusEntry=mscHgRowStatusEntry, huntGroupGroupCA=huntGroupGroupCA, mscHgProvEntry=mscHgProvEntry, mscHgProvTable=mscHgProvTable, mscHgHgMAdminState=mscHgHgMAdminState, huntGroupGroupCA02A=huntGroupGroupCA02A, mscHgHgMOperationalTable=mscHgHgMOperationalTable, mscHgHgMProvEntry=mscHgHgMProvEntry, mscHgAdminState=mscHgAdminState, mscHgFailedCalls=mscHgFailedCalls, mscHgUsageState=mscHgUsageState, mscHgMaxHuntAttempts=mscHgMaxHuntAttempts, mscHgHgMProvTable=mscHgHgMProvTable, mscHgAvailabilityUpdates=mscHgAvailabilityUpdates, mscHgOperationalTable=mscHgOperationalTable, huntGroupCapabilities=huntGroupCapabilities, mscHgHuntAttempts=mscHgHuntAttempts, mscHgCidDataTable=mscHgCidDataTable, mscHgHgMAvailabilityUpdates=mscHgHgMAvailabilityUpdates, mscHgAppendSuffixDigits=mscHgAppendSuffixDigits, mscHgHgMAvailability=mscHgHgMAvailability, mscHgHgMStorageType=mscHgHgMStorageType, mscHgSelectionPolicy=mscHgSelectionPolicy, mscHgInitialHuntAttempts=mscHgInitialHuntAttempts, mscHgAddress=mscHgAddress, mscHgOperationalEntry=mscHgOperationalEntry, huntGroupCapabilitiesCA02=huntGroupCapabilitiesCA02, mscHgHgMRowStatusEntry=mscHgHgMRowStatusEntry, huntGroupMIB=huntGroupMIB, mscHgBadPackets=mscHgBadPackets, mscHgHgMIndex=mscHgHgMIndex, mscHgHgMOperationalState=mscHgHgMOperationalState, mscHgCidDataEntry=mscHgCidDataEntry, huntGroupGroup=huntGroupGroup, mscHgStateEntry=mscHgStateEntry, mscHgRowStatus=mscHgRowStatus, mscHgStateTable=mscHgStateTable, mscHgRowStatusTable=mscHgRowStatusTable, mscHgHgMRowStatusTable=mscHgHgMRowStatusTable, mscHgNsapAddressEntry=mscHgNsapAddressEntry)
