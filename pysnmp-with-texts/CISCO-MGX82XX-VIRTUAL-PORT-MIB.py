#
# PySNMP MIB module CISCO-MGX82XX-VIRTUAL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX82XX-VIRTUAL-PORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
virtualInterface, = mibBuilder.importSymbols("BASIS-MIB", "virtualInterface")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, NotificationType, iso, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "NotificationType", "iso", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgx82xxVirtualPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 38))
ciscoMgx82xxVirtualPortMIB.setRevisions(('2002-08-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setRevisionsDescriptions(('Initial version of the MIB. The content of this MIB was originally available in CISCO-WAN-AXIPOP-MIB defined using SMIv1. The applicable objects from CISCO-WAN-AXIPOP-MIB are defined using SMIv2 in this MIB. Also the descriptions of some of the objects have been modified.',))
if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setLastUpdated('200208300000Z')
if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoMgx82xxVirtualPortMIB.setDescription('The MIB module for configuration ond reporting statistics of virtual ports in PXM1 Service module in MGX82xx series.')
virtualInterfaceCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1))
virtualInterfaceCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2))
virtualInterfaceQbinCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3))
virtualInterfaceQbinCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4))
vrtlIntrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1), )
if mibBuilder.loadTexts: vrtlIntrConfigTable.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrConfigTable.setDescription('Virtual Interface Configuration Table.')
vrtlIntrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "configVrtlIntrNum"))
if mibBuilder.loadTexts: vrtlIntrConfigEntry.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrConfigEntry.setDescription('An entry in the Virtual Interface configuration Table.')
configVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVrtlIntrNum.setStatus('current')
if mibBuilder.loadTexts: configVrtlIntrNum.setDescription('Virtual Interface Number. There are totaly. 32 Virtual Interfaces on the card (egress).')
vrtlIntrPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrPortNum.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrPortNum.setDescription('Port number which will be connected to the Virtual Interface. Value zero meens that this virtual interface is not connected to any port.')
vrtlIntrState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrState.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrState.setDescription('Virtual Interface State.')
vrtlIntrMaxQueMem = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrMaxQueMem.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrMaxQueMem.setDescription("Virtual Interface's Max queue memory. 1 = 4Kcells 2 = 8Kcells 3 = 16Kcells 4 = 32Kcells 5 = 64Kcells 6 = 128Kcells 7 = 256Kcells 8 = 512Kcells.")
vrtlIntrMinCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(103384, 353208))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrMinCellRate.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrMinCellRate.setDescription("Virtual Interface's minimum cell rate. The default value: for OC12 port is 1412832 cells/sec for OC3 port is 353208 cells/sec for T3 port is 96000 cells/sec for E3 port is 80000 cells/sec")
vrtlIntrMaxCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(103384, 353208))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrMaxCellRate.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrMaxCellRate.setDescription("Virtual Interface's maximum cell rate. The default value: for OC12 port is 1412832 cells/sec for OC3 port is 353208 cells/sec for T3 port is 96000 cells/sec for E3 port is 80000 cells/sec")
vrtlIntrCurrConfigPaths = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrCurrConfigPaths.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrCurrConfigPaths.setDescription('This is not a configurable parameter. This gives the count of paths currently configured on this virtual interface.')
vrtlIntrCounterTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1), )
if mibBuilder.loadTexts: vrtlIntrCounterTable.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrCounterTable.setDescription('Virtual Interface Counter32s Table.')
vrtlIntrCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "countVrtlIntrNum"))
if mibBuilder.loadTexts: vrtlIntrCounterEntry.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrCounterEntry.setDescription('An entry in the Virtual Interface Counter32 Table.')
countVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: countVrtlIntrNum.setStatus('current')
if mibBuilder.loadTexts: countVrtlIntrNum.setDescription('Virtual Interface Number.')
vrtlIntrTotalCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrTotalCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrTotalCellCnt.setDescription(' Total number of cells (VC plus Qbin) that belong to this Virtual Interface.')
vrtlIntrTotalQbinCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrTotalQbinCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrTotalQbinCellCnt.setDescription('Total number of cells in the Qbin belonging to this Virtual Interface.')
vrtlIntrRxdValidOAMCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdValidOAMCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrRxdValidOAMCellCnt.setDescription('Total number of OAM cell received.')
vrtlIntrRxdRmCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdRmCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrRxdRmCellCnt.setDescription('Total number of RM cells Received.')
vrtlIntrRxdClpUntaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpUntaggedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrRxdClpUntaggedCellCnt.setDescription('Total number of CLP-0 cells Received.')
vrtlIntrRxdClpTaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpTaggedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrRxdClpTaggedCellCnt.setDescription('Total number of CLP-1 cells Received.')
vrtlIntrRxdClpUntaggedDiscardedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpUntaggedDiscardedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrRxdClpUntaggedDiscardedCellCnt.setDescription('Total number of CLP-0 cells discarded at Ingress.')
vrtlIntrRxdClpTaggedDiscardedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrRxdClpTaggedDiscardedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrRxdClpTaggedDiscardedCellCnt.setDescription('Total number of CLP-1 cells discarded at Ingress.')
vrtlIntrXmtdOAMCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdOAMCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrXmtdOAMCellCnt.setDescription('Total number of OAM cells transmitted.')
vrtlIntrXmtdRmCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdRmCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrXmtdRmCellCnt.setDescription('Total number of RM(Resource Monitoring) cells transmitted.')
vrtlIntrXmtdClpUntaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdClpUntaggedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrXmtdClpUntaggedCellCnt.setDescription('Total number of CLP-0 cells transmitted.')
vrtlIntrXmtdClpTaggedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrXmtdClpTaggedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrXmtdClpTaggedCellCnt.setDescription('Total number of CLP-1 cells transmitted.')
vrtlIntrQbinConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1), )
if mibBuilder.loadTexts: vrtlIntrQbinConfigTable.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinConfigTable.setDescription('Virtual Interface QBin Configuration Table.')
vrtlIntrQbinConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrNum"), (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrQbinNum"))
if mibBuilder.loadTexts: vrtlIntrQbinConfigEntry.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinConfigEntry.setDescription('An entry in the Virtual Interface Qbin Config Table.')
queConfigVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queConfigVrtlIntrNum.setStatus('current')
if mibBuilder.loadTexts: queConfigVrtlIntrNum.setDescription(' Virtual Interface Number.')
queConfigVrtlIntrQbinNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queConfigVrtlIntrQbinNum.setStatus('current')
if mibBuilder.loadTexts: queConfigVrtlIntrQbinNum.setDescription(' Virtual Interface Qbin Number. There are totaly 16 Qbin per Virtual Interface.')
vrtlIntrQbinState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinState.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinState.setDescription('Virtual Interface QBIN state.')
vrtlIntrQbinPri = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinPri.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinPri.setDescription('This indicates the priority of the QBIN service within the Virtual Interface.')
vrtlIntrQbinRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 353208))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinRate.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinRate.setDescription('The rate at which cells in the QBIN are serviced. Max Cell rate for OC3 interface is 353208 cell/sec.')
vrtlIntrQbinDiscardSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("clpHysteresis", 1), ("frameDiscard", 3))).clone('clpHysteresis')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinDiscardSelection.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinDiscardSelection.setDescription(' Virtual Interface QBin Congestion control option.')
vrtlIntrQbinMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinMaxThreshold.setDescription('Max cells that can be queued in the QBIN. The Get value will be different from the Set value because of FW internal round up.')
vrtlIntrQbinClpHiThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinClpHiThreshold.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinClpHiThreshold.setDescription('The threshold above which the tagged cells will be dropped. The Get value will be different from the Set value because of FW internal round up.')
vrtlIntrQbinClpLoThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinClpLoThreshold.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinClpLoThreshold.setDescription('Valid only if congestion control is set to CLP hysterises. The threshold upto which the dropping of the tagged cells should continue once it has crossed CLP HI threshold. The Get value will be different from the Set value because of FW internal round up.')
vrtlIntrQbinFrameDiscardThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinFrameDiscardThreshold.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinFrameDiscardThreshold.setDescription('Valid only if congestion control is set to Frame Discard. It is the threshold after which the QE will start discarding the entire frame if one or more cells of the frame is discarded.. The Get value will be different from the Set value because of FW internal round up.')
vrtlIntrQbinEfciThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrtlIntrQbinEfciThreshold.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinEfciThreshold.setDescription('The threshold above which the EFCI bits of the cell is set. The Get value will be different from the Set value because of FW internal round up.')
vrtlIntrQbinCounterTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1), )
if mibBuilder.loadTexts: vrtlIntrQbinCounterTable.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinCounterTable.setDescription('Virtual Interface QBin Counter Table.')
vrtlIntrQbinCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConuterVrtlIntrNum"), (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queCounterVrtlIntrQbinNum"))
if mibBuilder.loadTexts: vrtlIntrQbinCounterEntry.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinCounterEntry.setDescription('An entry in the Virtual Interface Qbin Counter Table. Each entry contains information on the statistics supported for an interface.')
queConuterVrtlIntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queConuterVrtlIntrNum.setStatus('current')
if mibBuilder.loadTexts: queConuterVrtlIntrNum.setDescription(' Virtual Interface Number.')
queCounterVrtlIntrQbinNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queCounterVrtlIntrQbinNum.setStatus('current')
if mibBuilder.loadTexts: queCounterVrtlIntrQbinNum.setDescription('Virtual Interface Qbin Number. There are totaly 16 Qbin per Virtual Interface.')
vrtlIntrQbinCurrentCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinCurrentCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinCurrentCellCnt.setDescription(' Total number of cells currently in the Qbin.')
vrtlIntrQbinRxdCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinRxdCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinRxdCellCnt.setDescription(' Total number of cells arrived to the QBIN.')
vrtlIntrQbinTxdCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinTxdCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinTxdCellCnt.setDescription('Total number of cells departured from QBIN.')
vrtlIntrQbinDiscardedCellCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrtlIntrQbinDiscardedCellCnt.setStatus('current')
if mibBuilder.loadTexts: vrtlIntrQbinDiscardedCellCnt.setDescription('Total number of arrivals to QBIN which were discarded.')
cmvPortMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 38, 2))
cmvPortMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1))
cmvPortMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 2))
cmvPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 2, 1)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortConfGroup"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortStatsGroup"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortQbinConfGroup"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "cmvPortQbinStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortCompliance = cmvPortCompliance.setStatus('current')
if mibBuilder.loadTexts: cmvPortCompliance.setDescription('The compliance statement for objects related to SRM MIB.')
cmvPortConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 1)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "configVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrPortNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrState"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMaxQueMem"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMinCellRate"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMaxCellRate"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrCurrConfigPaths"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortConfGroup = cmvPortConfGroup.setStatus('current')
if mibBuilder.loadTexts: cmvPortConfGroup.setDescription('The collection of objects which are used for configuring Virtual Ports in PXM1 service module.')
cmvPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 2)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "countVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrTotalCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrTotalQbinCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdValidOAMCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdRmCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpUntaggedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpTaggedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpUntaggedDiscardedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpTaggedDiscardedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdOAMCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdRmCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdClpUntaggedCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdClpTaggedCellCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortStatsGroup = cmvPortStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cmvPortStatsGroup.setDescription('The collection of objects related to statistics for Virtual Ports in PXM1 service module.')
cmvPortQbinConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 3)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrQbinNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinState"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinPri"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinRate"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinDiscardSelection"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinMaxThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinClpHiThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinClpLoThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinFrameDiscardThreshold"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinEfciThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortQbinConfGroup = cmvPortQbinConfGroup.setStatus('current')
if mibBuilder.loadTexts: cmvPortQbinConfGroup.setDescription('The collection of objects related to configuration of Qbin related things in PXM1 service module.')
cmvPortQbinStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 4)).setObjects(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConuterVrtlIntrNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queCounterVrtlIntrQbinNum"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinCurrentCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinRxdCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinTxdCellCnt"), ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinDiscardedCellCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmvPortQbinStatsGroup = cmvPortQbinStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cmvPortQbinStatsGroup.setDescription('The collection of objects related to statistics for Qbin related things in PXM1 service module.')
mibBuilder.exportSymbols("CISCO-MGX82XX-VIRTUAL-PORT-MIB", vrtlIntrQbinClpLoThreshold=vrtlIntrQbinClpLoThreshold, queCounterVrtlIntrQbinNum=queCounterVrtlIntrQbinNum, vrtlIntrMaxCellRate=vrtlIntrMaxCellRate, vrtlIntrRxdClpTaggedCellCnt=vrtlIntrRxdClpTaggedCellCnt, vrtlIntrQbinCounterTable=vrtlIntrQbinCounterTable, cmvPortMIBConformance=cmvPortMIBConformance, vrtlIntrMaxQueMem=vrtlIntrMaxQueMem, PYSNMP_MODULE_ID=ciscoMgx82xxVirtualPortMIB, vrtlIntrConfigEntry=vrtlIntrConfigEntry, configVrtlIntrNum=configVrtlIntrNum, queConfigVrtlIntrQbinNum=queConfigVrtlIntrQbinNum, vrtlIntrQbinEfciThreshold=vrtlIntrQbinEfciThreshold, vrtlIntrQbinCounterEntry=vrtlIntrQbinCounterEntry, cmvPortStatsGroup=cmvPortStatsGroup, cmvPortQbinConfGroup=cmvPortQbinConfGroup, vrtlIntrRxdClpUntaggedCellCnt=vrtlIntrRxdClpUntaggedCellCnt, vrtlIntrQbinConfigTable=vrtlIntrQbinConfigTable, vrtlIntrRxdClpTaggedDiscardedCellCnt=vrtlIntrRxdClpTaggedDiscardedCellCnt, vrtlIntrXmtdClpUntaggedCellCnt=vrtlIntrXmtdClpUntaggedCellCnt, vrtlIntrXmtdClpTaggedCellCnt=vrtlIntrXmtdClpTaggedCellCnt, vrtlIntrTotalCellCnt=vrtlIntrTotalCellCnt, vrtlIntrCurrConfigPaths=vrtlIntrCurrConfigPaths, ciscoMgx82xxVirtualPortMIB=ciscoMgx82xxVirtualPortMIB, vrtlIntrQbinTxdCellCnt=vrtlIntrQbinTxdCellCnt, vrtlIntrRxdRmCellCnt=vrtlIntrRxdRmCellCnt, virtualInterfaceCnt=virtualInterfaceCnt, vrtlIntrQbinDiscardSelection=vrtlIntrQbinDiscardSelection, virtualInterfaceCnf=virtualInterfaceCnf, cmvPortQbinStatsGroup=cmvPortQbinStatsGroup, vrtlIntrQbinPri=vrtlIntrQbinPri, vrtlIntrMinCellRate=vrtlIntrMinCellRate, vrtlIntrQbinMaxThreshold=vrtlIntrQbinMaxThreshold, queConuterVrtlIntrNum=queConuterVrtlIntrNum, queConfigVrtlIntrNum=queConfigVrtlIntrNum, vrtlIntrQbinRxdCellCnt=vrtlIntrQbinRxdCellCnt, vrtlIntrRxdClpUntaggedDiscardedCellCnt=vrtlIntrRxdClpUntaggedDiscardedCellCnt, vrtlIntrQbinFrameDiscardThreshold=vrtlIntrQbinFrameDiscardThreshold, cmvPortConfGroup=cmvPortConfGroup, vrtlIntrXmtdOAMCellCnt=vrtlIntrXmtdOAMCellCnt, vrtlIntrQbinRate=vrtlIntrQbinRate, vrtlIntrConfigTable=vrtlIntrConfigTable, virtualInterfaceQbinCnf=virtualInterfaceQbinCnf, vrtlIntrCounterEntry=vrtlIntrCounterEntry, vrtlIntrQbinState=vrtlIntrQbinState, vrtlIntrState=vrtlIntrState, vrtlIntrRxdValidOAMCellCnt=vrtlIntrRxdValidOAMCellCnt, vrtlIntrTotalQbinCellCnt=vrtlIntrTotalQbinCellCnt, vrtlIntrXmtdRmCellCnt=vrtlIntrXmtdRmCellCnt, cmvPortMIBGroups=cmvPortMIBGroups, vrtlIntrQbinCurrentCellCnt=vrtlIntrQbinCurrentCellCnt, vrtlIntrQbinConfigEntry=vrtlIntrQbinConfigEntry, vrtlIntrCounterTable=vrtlIntrCounterTable, countVrtlIntrNum=countVrtlIntrNum, vrtlIntrQbinDiscardedCellCnt=vrtlIntrQbinDiscardedCellCnt, cmvPortMIBCompliances=cmvPortMIBCompliances, virtualInterfaceQbinCnt=virtualInterfaceQbinCnt, cmvPortCompliance=cmvPortCompliance, vrtlIntrQbinClpHiThreshold=vrtlIntrQbinClpHiThreshold, vrtlIntrPortNum=vrtlIntrPortNum)
