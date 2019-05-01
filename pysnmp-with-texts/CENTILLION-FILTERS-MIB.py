#
# PySNMP MIB module CENTILLION-FILTERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-FILTERS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
StatusIndicator, sysConfig = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "StatusIndicator", "sysConfig")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, MibIdentifier, Gauge32, ObjectIdentity, Unsigned32, NotificationType, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class GeneralFilterName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NetbiosFilterName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class NetbiosFilterAction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("discard", 1), ("forward", 2))

filterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11))
filterGroupTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1), )
if mibBuilder.loadTexts: filterGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupTable.setDescription('Filter Group Table. Entries are added into the group by specifying values for all objects with the exception of the filterGroupMonitorDests and filterGroupAdditionalDests objects. Entries are deleted simply by specifying the appropriate filterGroupStatus value.')
filterGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1), ).setIndexNames((0, "CENTILLION-FILTERS-MIB", "filterGroupName"), (0, "CENTILLION-FILTERS-MIB", "filterGroupIndex"))
if mibBuilder.loadTexts: filterGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupEntry.setDescription('An entry in the filter group table. Table entries are indexed by the unique user-defined group name, and the filter entry index as assigned by the system.')
filterGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 1), GeneralFilterName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupName.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupName.setDescription('A user-defined unique ASCII string identifying the filter group.')
filterGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupIndex.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupIndex.setDescription('The index of the filter entry within the filter group. Any filter group entry is uniquely identifable by the group nam and index.')
filterGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 3), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupStatus.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupStatus.setDescription('The status of this filter group entry. Entries may be deleted by setting this object to invalid(2).')
filterGroupMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("lt", 1), ("eq", 2), ("le", 3), ("gt", 4), ("ne", 5), ("ge", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupMatch.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupMatch.setDescription('The match condition for the filter. Match conditions are in the form of the usual logical operators.')
filterGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("macFilter", 1), ("llcFilter", 2), ("vlanFilter", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupType.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupType.setDescription("The type of filter. MAC filters are defined from the start of the MAC frame. LLC filters are defined from the start of the LLC header (after RIF). VLAN filters operate on a packet's VLAN classification parameters. For a valid VLAN filter, filterGroupOffset be set to 0, and filterGroupValue must contain exactly four bytes of VLAN filter data as shown below: Octet 1 Defines the user priority match criteria for VLAN filter. Valid values are 0x01 through 0xFF. Each bit in the octet corresponds to one of the eight available user priority level as defined by the 802.1Q draft specification. The least significant bit represents priority zero, and the most significant bit represents priority seven. Octet 2 Defines the Canonical Format Indicator (CFI) match criteria for VLAN filter. Possible values are 0x00, 0x01 and 0xFF. The value 0xFF indicates the switch should ignore CFI value when filtering. Octet 3 and 4 Define 12-bit VLAN ID match criteria for VLAN filter. Valid values are 0x001 through 0xFFF.")
filterGroupOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupOffset.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupOffset.setDescription('The byte offset from the beginning of the header to the value to filter.')
filterGroupValue = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupValue.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupValue.setDescription('The filter value field. The value is specified as a hexadecimal string up to 12 bytes.')
filterGroupForward = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("normClear", 1), ("alt", 2), ("add", 3), ("addAlt", 4), ("norm", 5), ("normAlt", 6), ("normAdd", 7), ("normAddAlt", 8), ("drop", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupForward.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupForward.setDescription('The forwarding rule for the filter. Forward to normal indicates that the frame should be forwarded as usual.')
filterGroupNextIfMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupNextIfMatch.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupNextIfMatch.setDescription('The next filter entry as referenced by the filter index to apply if the filter match succeeds. An entry of 0 indicates that filtering ends for the packet. An entry whose value is larger than the number of filters in the group indicates that the next filter entry to apply is the next filter group (if any) enabled on the port.')
filterGroupNextIfFail = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupNextIfFail.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupNextIfFail.setDescription('The next filter entry as referenced by the filter index to apply if the filter match fails. An entry of 0 indicates that filtering ends for the packet. An entry whose value is larger than the number of filters in the group indicates that the next filter entry to apply is the next filter group (if any) enabled on the port.')
filterGroupAdditionalDests = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupAdditionalDests.setStatus('deprecated')
if mibBuilder.loadTexts: filterGroupAdditionalDests.setDescription('This will be replaced by filterGroupAdditionalDestions. A list of up to 256 pairs of additional cards and ports to send packets matching this filter. Each unsigned int8 is formatted as follows: the high-order 4 bits represent the card number, the low order 4 bits are the port number.')
filterGroupMonitorDests = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupMonitorDests.setStatus('deprecated')
if mibBuilder.loadTexts: filterGroupMonitorDests.setDescription('This will be replaced by filterGroupAlternateDestination. A pair of the monitoring card and port to send packets matching this filter. Each unsigned int8 is formatted as follows: the high-order 4 bits represent the card number, the low order 4 bits are the port number.')
filterGroupAdditionalDestinations = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupAdditionalDestinations.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupAdditionalDestinations.setDescription('For 24 ports support. This is to replace filterGroupAdditionalDests. Setting either filterGroupAdditionalDests or filterGroupAlternateDestination is enough. And if both are set, the one set later will be in effect. Make sure that even number of octets are given. A list of up to 256 pairs of additional cards and ports to send packets matching this filter. Each pair of octets is formatted as follows: the high-order octet represent the card number, the low order octet is the port number.')
filterGroupAlternateDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterGroupAlternateDestination.setStatus('mandatory')
if mibBuilder.loadTexts: filterGroupAlternateDestination.setDescription('For 24 ports support. This is to replace filterGroupMonitorDests. Setting either filterGroupMonitorDests filterGroupAlternateDestination is enough. And if both are set, the one set later will be in effect. Make sure that even number of octets are given. A pair of the monitoring card and port to send packets matching this filter. Each pair of octets is formatted as follows: the high-order byte represent the card number, the low order byte is the port number.')
filterPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2), )
if mibBuilder.loadTexts: filterPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortTable.setDescription('Input Filter Port Table.')
filterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1), ).setIndexNames((0, "CENTILLION-FILTERS-MIB", "filterPortCardNumber"), (0, "CENTILLION-FILTERS-MIB", "filterPortPortNumber"), (0, "CENTILLION-FILTERS-MIB", "filterPortIndex"))
if mibBuilder.loadTexts: filterPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortEntry.setDescription('An entry in the filter group table. Table entries are indexed by the unique user-defined group name, and the filter entry index as assigned by the system.')
filterPortCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortCardNumber.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortCardNumber.setDescription('The card number to which the filters apply.')
filterPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortPortNumber.setDescription('The port number to which the filters apply.')
filterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortIndex.setDescription('A unique value for each filter group within the port.')
filterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 4), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortStatus.setDescription('The status of this filter port entry. Entries may be deleted by setting this object to invalid(2).')
filterPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 2, 1, 5), GeneralFilterName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortGroupName.setStatus('mandatory')
if mibBuilder.loadTexts: filterPortGroupName.setDescription('The filter port group name.')
netbiosFilterPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3), )
if mibBuilder.loadTexts: netbiosFilterPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortTable.setDescription('The NetBIOS name filter table indexed by card and port numbers. ')
netbiosFilterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1), ).setIndexNames((0, "CENTILLION-FILTERS-MIB", "netbiosFilterPortCardNumber"), (0, "CENTILLION-FILTERS-MIB", "netbiosFilterPortPortNumber"), (0, "CENTILLION-FILTERS-MIB", "netbiosFilterPortIndex"))
if mibBuilder.loadTexts: netbiosFilterPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortEntry.setDescription('An entry in the NetBios filter port table. Table entries are indexed by the card, port and PortIndex as assigned by the system.')
netbiosFilterPortCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterPortCardNumber.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortCardNumber.setDescription('The card number to which the filters apply.')
netbiosFilterPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterPortPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortPortNumber.setDescription('The port number to which the filters apply.')
netbiosFilterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortIndex.setDescription('A unique value for each filter group within the port.')
netbiosFilterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 4), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortStatus.setDescription('The status of this NetBIOS filter entry. Entries may be deleted by setting this object to invalid(2).')
netbiosFilterPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 5), NetbiosFilterName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterPortName.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortName.setDescription('The NetBIOS name to match for filtering. The name will be blank padded.')
netbiosFilterPortAction = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 3, 1, 6), NetbiosFilterAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterPortAction.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterPortAction.setDescription('The action to take upon matching the name filter.')
netbiosFilterRingTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4), )
if mibBuilder.loadTexts: netbiosFilterRingTable.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingTable.setDescription('The NetBIOS name filter table indexed by ring number.')
netbiosFilterRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1), ).setIndexNames((0, "CENTILLION-FILTERS-MIB", "netbiosFilterRingNumber"), (0, "CENTILLION-FILTERS-MIB", "netbiosFilterRingIndex"))
if mibBuilder.loadTexts: netbiosFilterRingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingEntry.setDescription('An entry in the NetBios filter port table. Table entries are indexed by ring number and PortIndex as assigned by the system.')
netbiosFilterRingNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterRingNumber.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingNumber.setDescription('The ring number to which the filters apply.')
netbiosFilterRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterRingIndex.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingIndex.setDescription('A unique value for each filter group within the port.')
netbiosFilterRingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 3), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterRingStatus.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingStatus.setDescription('The status of this NetBIOS filter entry. Entries may be deleted by setting this object to invalid(2).')
netbiosFilterRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 4), NetbiosFilterName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterRingName.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingName.setDescription('The NetBIOS name to match for filtering. The name will be blank padded.')
netbiosFilterRingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 4, 1, 5), NetbiosFilterAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netbiosFilterRingAction.setStatus('mandatory')
if mibBuilder.loadTexts: netbiosFilterRingAction.setDescription('The action to take upon matching the name filter.')
outputFilterPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5), )
if mibBuilder.loadTexts: outputFilterPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortTable.setDescription('Output Filter Port Table.')
outputFilterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1), ).setIndexNames((0, "CENTILLION-FILTERS-MIB", "outputFilterPortCardNumber"), (0, "CENTILLION-FILTERS-MIB", "outputFilterPortPortNumber"), (0, "CENTILLION-FILTERS-MIB", "outputFilterPortIndex"))
if mibBuilder.loadTexts: outputFilterPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortEntry.setDescription('An entry in the filter group table. Table entries are indexed by the unique user-defined group name, and the filter entry index as assigned by the system.')
outputFilterPortCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outputFilterPortCardNumber.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortCardNumber.setDescription('The card number to which the filters apply.')
outputFilterPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outputFilterPortPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortPortNumber.setDescription('The port number to which the filters apply.')
outputFilterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outputFilterPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortIndex.setDescription('A unique value for each filter group within the port.')
outputFilterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 4), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outputFilterPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortStatus.setDescription('The status of this filter port entry. Entries may be deleted by setting this object to invalid(2).')
outputFilterPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 11, 5, 1, 5), GeneralFilterName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outputFilterPortGroupName.setStatus('mandatory')
if mibBuilder.loadTexts: outputFilterPortGroupName.setDescription('The filter port group name.')
mibBuilder.exportSymbols("CENTILLION-FILTERS-MIB", netbiosFilterPortName=netbiosFilterPortName, filterGroupValue=filterGroupValue, netbiosFilterRingName=netbiosFilterRingName, filterGroupOffset=filterGroupOffset, netbiosFilterPortCardNumber=netbiosFilterPortCardNumber, NetbiosFilterName=NetbiosFilterName, netbiosFilterRingTable=netbiosFilterRingTable, netbiosFilterPortPortNumber=netbiosFilterPortPortNumber, outputFilterPortIndex=outputFilterPortIndex, filterGroupForward=filterGroupForward, outputFilterPortPortNumber=outputFilterPortPortNumber, filterGroupName=filterGroupName, filterGroupNextIfMatch=filterGroupNextIfMatch, filterGroupAdditionalDests=filterGroupAdditionalDests, netbiosFilterPortAction=netbiosFilterPortAction, outputFilterPortTable=outputFilterPortTable, netbiosFilterRingIndex=netbiosFilterRingIndex, outputFilterPortEntry=outputFilterPortEntry, netbiosFilterPortIndex=netbiosFilterPortIndex, outputFilterPortCardNumber=outputFilterPortCardNumber, netbiosFilterRingNumber=netbiosFilterRingNumber, filterPortStatus=filterPortStatus, netbiosFilterRingAction=netbiosFilterRingAction, filterGroup=filterGroup, netbiosFilterPortStatus=netbiosFilterPortStatus, filterGroupIndex=filterGroupIndex, netbiosFilterPortTable=netbiosFilterPortTable, filterPortEntry=filterPortEntry, filterGroupTable=filterGroupTable, filterPortTable=filterPortTable, filterGroupMatch=filterGroupMatch, GeneralFilterName=GeneralFilterName, netbiosFilterPortEntry=netbiosFilterPortEntry, netbiosFilterRingStatus=netbiosFilterRingStatus, outputFilterPortGroupName=outputFilterPortGroupName, filterGroupType=filterGroupType, filterGroupMonitorDests=filterGroupMonitorDests, filterPortCardNumber=filterPortCardNumber, filterGroupStatus=filterGroupStatus, filterGroupAlternateDestination=filterGroupAlternateDestination, filterPortGroupName=filterPortGroupName, filterPortPortNumber=filterPortPortNumber, filterGroupEntry=filterGroupEntry, outputFilterPortStatus=outputFilterPortStatus, filterGroupAdditionalDestinations=filterGroupAdditionalDestinations, netbiosFilterRingEntry=netbiosFilterRingEntry, filterPortIndex=filterPortIndex, filterGroupNextIfFail=filterGroupNextIfFail, NetbiosFilterAction=NetbiosFilterAction)
