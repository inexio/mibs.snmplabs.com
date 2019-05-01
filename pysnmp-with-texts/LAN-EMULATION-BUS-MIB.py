#
# PySNMP MIB module LAN-EMULATION-BUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LAN-EMULATION-BUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
atmfLanEmulation, VciInteger, VpiInteger = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "atmfLanEmulation", "VciInteger", "VpiInteger")
Integer, AtmLaneMask, IfIndexOrZero, TIMESTAMP = mibBuilder.importSymbols("LAN-EMULATION-ELAN-MIB", "Integer", "AtmLaneMask", "IfIndexOrZero", "TIMESTAMP")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Bits, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, Gauge32, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "IpAddress", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
busMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 4))
class RowStatus(Integer32):
    pass

class AtmLaneAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(20, 20), )
busConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1))
busStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2))
busFaultGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3))
busConfNextId = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busConfNextId.setStatus('mandatory')
if mibBuilder.loadTexts: busConfNextId.setDescription('The next available BUS index. The value of this object can be used as the index by the network manager to create an entry in the busConfTable.')
busConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2), )
if mibBuilder.loadTexts: busConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: busConfTable.setDescription('This table contains all LAN Emulation Broadcast and Unknown Servers (BUS) this agent manages. The BUS handles data sent by an LE Client to the broadcast MAC address, all multicast traffic, and initial unicast frames which are sent by a LEC before the data direct target ATM address has been resolved. There can be multiple BUSs per ELAN, but a BUS can service only one ELAN.')
busConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"))
if mibBuilder.loadTexts: busConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busConfEntry.setDescription("Each entry in this table represents a BUS. The parameters in each entry apply to one emulated LAN served by one BUS. Object busRowStatus is required during row creation and deletion. Object busElanName is used to indicate the ELAN this BUS is servicing and is used to cross reference tables defined in the LAN Emulation Server MIB. Note that objects busAtmAddrSpec and busAtmAddrMask are used to configure the ATM address of a BUS. The BUS typically derives it's ATM address from the switch or the network and the actual ATM address used is indicated in the object busAtmAddrActual.")
busConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: busConfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: busConfIndex.setDescription('A value which uniquely identifies a conceptual row in the busConfTable. If the conceptual row identified by this value of busConfIndex is recreated following an agent restart, the same value of busConfIndex must be used to identify the recreated row.')
busConfAtmAddrSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 2), AtmLaneAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busConfAtmAddrSpec.setStatus('mandatory')
if mibBuilder.loadTexts: busConfAtmAddrSpec.setDescription('An ATM address specified by the network or local management that, with the ATM address mask, determines a portion of the ATM address that the BUS on the designated ATM interface will use to derive the actual ATM address from the network or ILMI. The derived ATM address is specified in the object busAtmAddrActual, which is used to receive multicast or broadcast traffic.')
busConfAtmAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 3), AtmLaneMask().clone(hexValue="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busConfAtmAddrMask.setStatus('mandatory')
if mibBuilder.loadTexts: busConfAtmAddrMask.setDescription("The ATM address mask associated with the object busAtmAddrSpec. The value of the mask is an ATM address with the don't care portion set to zero and the valid ATM address portion set to one.")
busConfAtmAddrActual = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 4), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busConfAtmAddrActual.setStatus('mandatory')
if mibBuilder.loadTexts: busConfAtmAddrActual.setDescription(' The resultant ATM address in use by the BUS. This object is a product of the specified ATM address, mask and interaction with the network. This object is created by the agent.')
busConfElanName = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busConfElanName.setStatus('mandatory')
if mibBuilder.loadTexts: busConfElanName.setDescription('The name of the ELAN this BUS is providing service to.')
busConfLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 6), TIMESTAMP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busConfLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: busConfLastChange.setDescription('The value of the sysUpTime when this BUS has entered the state indicated by the object busConfOperStatus.')
busConfMaxFrameAge = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busConfMaxFrameAge.setReference('LAN Emulation Over ATM Specification - version 1.0. S5.')
if mibBuilder.loadTexts: busConfMaxFrameAge.setStatus('mandatory')
if mibBuilder.loadTexts: busConfMaxFrameAge.setDescription('Time out period for a frame that has been received but not been transmitted by BUS to all relevant Multicast Send VCCs or Multicast Forward VCCs.')
busConfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busConfOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busConfOperStatus.setDescription("The operational state of this BUS entry. When in 'up' state the BUS will forward LEC traffic. Any other state the BUS is not available for service and may release all the existing VCCs and refuse service to all clients.")
busConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("up", 2), ("down", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busConfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busConfAdminStatus.setDescription(' The desired state of the designated BUS as prescribed by the operator. The actions of the agent will, if at all possible, eventually result in the desired state being reflected in the busOperStatus.')
busConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busConfRowStatus.setReference('RFC 1443, [10] Textual Conventions for version 2 of the Simple Network Management Protocol (SNMPv2).')
if mibBuilder.loadTexts: busConfRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busConfRowStatus.setDescription('This object is used to create or delete entries in the busConfTable.')
busVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3), )
if mibBuilder.loadTexts: busVccTable.setStatus('mandatory')
if mibBuilder.loadTexts: busVccTable.setDescription('This table contains all the Multicast Forward VCCs used by the BUS to forward multicast traffic to the participating LECs. The Multicast Forward VCC can either be point-to-point or point-to- multipoint calls. This table is read only if SVCs are used and writable if PVCs are used.')
busVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"), (0, "LAN-EMULATION-BUS-MIB", "busVccAtmIfIndex"), (0, "LAN-EMULATION-BUS-MIB", "busVccMtFwdVpi"), (0, "LAN-EMULATION-BUS-MIB", "busVccMtFwdVci"))
if mibBuilder.loadTexts: busVccEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busVccEntry.setDescription('Each entry in this table represents a Multicast Forward VCC of the BUS.')
busVccAtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 1), IfIndexOrZero())
if mibBuilder.loadTexts: busVccAtmIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: busVccAtmIfIndex.setDescription('The ATM interface which the Multicast Forward VCC is running on. This value must match an existing value in the ifTable. The value of this object is set to zero when the ATM interface is undefined.')
busVccMtFwdVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 2), VpiInteger())
if mibBuilder.loadTexts: busVccMtFwdVpi.setStatus('mandatory')
if mibBuilder.loadTexts: busVccMtFwdVpi.setDescription('The VPI value of the Multicast Forward VCC. The object busVccAtmIfIndex, busVccMtFwdVci and the value of this object uniquely identfies a VCC within a ATM host.')
busVccMtFwdVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 3), VciInteger())
if mibBuilder.loadTexts: busVccMtFwdVci.setStatus('mandatory')
if mibBuilder.loadTexts: busVccMtFwdVci.setDescription('The VCI value of the Multicast Forward VCC. The object busVccAtmIfIndex, busVccMtFwdVpi and the value of this object uniquely identfies a VCC within a ATM host.')
busVccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busVccRowStatus.setReference('RFC 1443, [10] Textual Conventions for version 2 of the Simple Network Management Protocol (SNMPv2).')
if mibBuilder.loadTexts: busVccRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busVccRowStatus.setDescription('This object is used to create or delete entries in the busConfTable.')
busLecTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 4), TIMESTAMP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busLecTableLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: busLecTableLastChange.setDescription('The value of sysUpTime when an entry of the busLecTable was created/deleted.')
busLecTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5), )
if mibBuilder.loadTexts: busLecTable.setStatus('mandatory')
if mibBuilder.loadTexts: busLecTable.setDescription(' This table contains the BUS and the actual LECs being serviced by the BUS. It can be used as the actual mapping between BUS and LEC. This table provides information for Multicast send VCCs between BUS and clients. Objects busLecMcastSendAtmIfIndex, busLecMcastSendVpi, and busLecMcstSendVci can only be modified if PVC is used.')
busLecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"), (0, "LAN-EMULATION-BUS-MIB", "busLecAtmAddr"))
if mibBuilder.loadTexts: busLecEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busLecEntry.setDescription('Each entry represents a BUS to LEC mapping.')
busLecAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 1), AtmLaneAddress())
if mibBuilder.loadTexts: busLecAtmAddr.setStatus('mandatory')
if mibBuilder.loadTexts: busLecAtmAddr.setDescription('The ATM address of the LEC. This is the primary ATM address of the LEC.')
busLecMcastSendAtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 2), IfIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busLecMcastSendAtmIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: busLecMcastSendAtmIfIndex.setDescription('The ATM interface index this BUS uses for Multicast Send traffic. The value of this object has to exist in the ifTable in MIB II unless an internal connection is used. When an internal connection is used, this object is set to zero.')
busLecMcastSendVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 4), VpiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busLecMcastSendVpi.setStatus('mandatory')
if mibBuilder.loadTexts: busLecMcastSendVpi.setDescription(' The virtual path identifier used to receive multicast traffic by this BUS.')
busLecMcastSendVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 5), VciInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busLecMcastSendVci.setStatus('mandatory')
if mibBuilder.loadTexts: busLecMcastSendVci.setDescription(' The virtual channel identifier used to receive multicast traffic by this BUS.')
busLecRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busLecRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busLecRowStatus.setDescription(' This object provides a way for the network manager to selectively remove a LE Client from the designated BUS. Or in a system where PVCs are used, this table is used to create Multicast Send VCCs between BUS and LEC.')
busStatTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1), )
if mibBuilder.loadTexts: busStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: busStatTable.setDescription('This table contains all counters the BUS maintain. This table is an extention to the busConfTable.')
busStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"))
if mibBuilder.loadTexts: busStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busStatEntry.setDescription('Each entry in this table contains a BUS and its counters.')
busStatInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatInDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: busStatInDiscards.setDescription(' The number of frames discarded due to resource error.')
busStatInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: busStatInOctets.setDescription(' The number of octets that this BUS has received since its initialization.')
busStatInUcastFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatInUcastFrms.setStatus('mandatory')
if mibBuilder.loadTexts: busStatInUcastFrms.setDescription(' The number of frames that the BUS has received which were unicast data frames and all control frames (i.e. they were flooded from the client).')
busStatInMcastFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatInMcastFrms.setStatus('mandatory')
if mibBuilder.loadTexts: busStatInMcastFrms.setDescription(' The number of frames that the BUS has received which were multicast frames.')
busStatFrmTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatFrmTimeOuts.setStatus('mandatory')
if mibBuilder.loadTexts: busStatFrmTimeOuts.setDescription(' The number of frames dropped by the BUS due to time out.')
busStatMcastSendRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatMcastSendRefused.setStatus('mandatory')
if mibBuilder.loadTexts: busStatMcastSendRefused.setDescription(' The number of multicast send VCCconnection setup attempts to the BUS which were refused.')
busStatMcastFwdFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busStatMcastFwdFailure.setStatus('mandatory')
if mibBuilder.loadTexts: busStatMcastFwdFailure.setDescription(' The number of multicast forward VCCconnection setup attempts from the BUS which were unsuccessful for any reason.')
busLecStatTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2), )
if mibBuilder.loadTexts: busLecStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: busLecStatTable.setDescription('This table contains all LEC counters the BUS maintains. This table can also be used to retrieve all LECs a BUS is providing service to.')
busLecStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"), (0, "LAN-EMULATION-BUS-MIB", "busLecAtmAddr"))
if mibBuilder.loadTexts: busLecStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busLecStatEntry.setDescription('Each entry in this table represents a LEC and its counters.')
busLecRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busLecRecvs.setStatus('mandatory')
if mibBuilder.loadTexts: busLecRecvs.setDescription('Number of Multicast, Broadcast and Unknown Forward requests received by the BUS from this LEC.')
busLecForwards = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busLecForwards.setStatus('mandatory')
if mibBuilder.loadTexts: busLecForwards.setDescription('Number of Multicast, Broadcast and Unkown Forward requests forwarded by the BUS from this LEC. The value of this object indicate how many requests have been forwarded by the BUS.')
busLecDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busLecDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: busLecDiscards.setDescription('Number of Multicast, Broadcast and Unkown Forward requests discarded by the BUS from this LEC. The value of this object indicate how many requests have been discarded by the BUS.')
busErrCtlTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1), )
if mibBuilder.loadTexts: busErrCtlTable.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlTable.setDescription('This table contains error log control information of all BUS instances. This table is an extention to the busConfTable. It is used to enable or disable error logs for a particular BUS entry.')
busErrCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"))
if mibBuilder.loadTexts: busErrCtlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlEntry.setDescription('Each entry represents a BUS entry in the busConfTable.')
busErrCtlAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busErrCtlAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlAdminStatus.setDescription('This object is used to enable/disable error logging for the BUS.')
busErrCtlOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("outOfRes", 3), ("failed", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busErrCtlOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlOperStatus.setDescription('This object is used to indicate the result of a set operation to the object busErrCtlAdminStatus. If the error log was successfully started, it is in active(2) mode. Otherwise, it is set to either outOfRes(3) or failed(4) for the respective reasons.')
busErrCtlClearLog = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busErrCtlClearLog.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlClearLog.setDescription('This object is used to clear the error log entries associated with this BUS.')
busErrCtlMaxEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busErrCtlMaxEntries.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlMaxEntries.setDescription('The maximum entries of the error log a BUS can support.')
busErrCtlLastEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: busErrCtlLastEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busErrCtlLastEntry.setDescription('The index to the last entry in the error log table for this BUS.')
busErrLogTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2), )
if mibBuilder.loadTexts: busErrLogTable.setStatus('mandatory')
if mibBuilder.loadTexts: busErrLogTable.setDescription('This table contains error logs of the BUS instances enabled in the busErrCtlTable. This table is indexed by the BUS instance index and an arbitrary integer uniquely identifies an error log.')
busErrLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1), ).setIndexNames((0, "LAN-EMULATION-BUS-MIB", "busConfIndex"), (0, "LAN-EMULATION-BUS-MIB", "busErrLogIndex"))
if mibBuilder.loadTexts: busErrLogEntry.setStatus('mandatory')
if mibBuilder.loadTexts: busErrLogEntry.setDescription('Each entry represents aan error detected by the BUS.')
busErrLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: busErrLogIndex.setStatus('mandatory')
if mibBuilder.loadTexts: busErrLogIndex.setDescription('An arbitrary integer which uniquely identifies an error log entry. The first entry after reset or clearing the error log is an assigned value (2^32-1). Succeding entries are assigned with descending values consecutively. Entries after 1 are discarded.The enabling/disabling of the error log capability is done in the busErrCtlTable.')
busErrLogAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 2), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busErrLogAtmAddr.setStatus('mandatory')
if mibBuilder.loadTexts: busErrLogAtmAddr.setDescription('The primary ATM address of the LE Client on whose Multicast Send VCC the error occured. The corresponding error code is specified in the object busErrLogErrCode.')
busErrLogErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("outOfRes", 1), ("badCtlFrame", 2), ("badDataFrame", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busErrLogErrCode.setStatus('mandatory')
if mibBuilder.loadTexts: busErrLogErrCode.setDescription('The Error code which indicates the cause of the error.')
busErrLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 4), TIMESTAMP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busErrLogTime.setStatus('mandatory')
if mibBuilder.loadTexts: busErrLogTime.setDescription('The sysUpTime when this entry was logged by the BUS.')
mibBuilder.exportSymbols("LAN-EMULATION-BUS-MIB", busLecDiscards=busLecDiscards, busConfGroup=busConfGroup, busConfEntry=busConfEntry, busErrCtlOperStatus=busErrCtlOperStatus, busStatInDiscards=busStatInDiscards, busConfTable=busConfTable, busConfLastChange=busConfLastChange, busConfMaxFrameAge=busConfMaxFrameAge, busVccMtFwdVpi=busVccMtFwdVpi, busConfElanName=busConfElanName, busMIB=busMIB, busLecMcastSendVpi=busLecMcastSendVpi, busStatGroup=busStatGroup, busLecRowStatus=busLecRowStatus, busStatInMcastFrms=busStatInMcastFrms, busStatFrmTimeOuts=busStatFrmTimeOuts, busErrLogAtmAddr=busErrLogAtmAddr, busErrLogErrCode=busErrLogErrCode, busLecStatTable=busLecStatTable, busLecStatEntry=busLecStatEntry, busErrLogTable=busErrLogTable, busLecTableLastChange=busLecTableLastChange, busLecAtmAddr=busLecAtmAddr, AtmLaneAddress=AtmLaneAddress, busStatTable=busStatTable, busStatInOctets=busStatInOctets, busLecEntry=busLecEntry, busConfOperStatus=busConfOperStatus, busLecMcastSendVci=busLecMcastSendVci, busVccTable=busVccTable, busErrCtlTable=busErrCtlTable, busErrCtlAdminStatus=busErrCtlAdminStatus, busErrCtlClearLog=busErrCtlClearLog, busVccEntry=busVccEntry, busStatInUcastFrms=busStatInUcastFrms, busConfRowStatus=busConfRowStatus, busErrCtlLastEntry=busErrCtlLastEntry, busLecTable=busLecTable, busErrLogEntry=busErrLogEntry, busLecRecvs=busLecRecvs, busErrCtlEntry=busErrCtlEntry, busFaultGroup=busFaultGroup, busErrCtlMaxEntries=busErrCtlMaxEntries, busVccAtmIfIndex=busVccAtmIfIndex, busErrLogIndex=busErrLogIndex, busConfIndex=busConfIndex, busVccRowStatus=busVccRowStatus, busStatMcastSendRefused=busStatMcastSendRefused, RowStatus=RowStatus, busLecMcastSendAtmIfIndex=busLecMcastSendAtmIfIndex, busConfAtmAddrSpec=busConfAtmAddrSpec, busConfAtmAddrMask=busConfAtmAddrMask, busLecForwards=busLecForwards, busVccMtFwdVci=busVccMtFwdVci, busStatMcastFwdFailure=busStatMcastFwdFailure, busConfAtmAddrActual=busConfAtmAddrActual, busConfAdminStatus=busConfAdminStatus, busConfNextId=busConfNextId, busErrLogTime=busErrLogTime, busStatEntry=busStatEntry)
