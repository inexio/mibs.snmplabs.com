#
# PySNMP MIB module NTNTECH-CHASSIS-CONFIGURATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-CHASSIS-CONFIGURATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NtnDisplayString, NtnTimeTicks, NtnDefaultGateway, ntntechChassis, NtnSubnetMask = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "NtnDisplayString", "NtnTimeTicks", "NtnDefaultGateway", "ntntechChassis", "NtnSubnetMask")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, ObjectIdentity, ModuleIdentity, IpAddress, Bits, TimeTicks, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntntechChassisConfigurationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1))
ntntechChassisConfigurationMIB.setRevisions(('1902-08-13 11:12', '1902-08-28 09:12', '1902-10-11 09:13', '1902-10-22 02:00', '1902-11-04 12:58', '1904-03-15 10:15', '1904-04-27 11:16', '1904-10-11 09:09', '1904-11-17 09:58',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setRevisionsDescriptions(('Added the mumCfgAdvanced OID. Added the mumCfgManagementPort OID.', 'New Release - v1.01.00', 'Added OID mgmtPortCfgType to the mgmtPortCfgTable.', 'New Release - v1.01.01', 'Added the values uplink3(4), uplink4(5), and mgmt(6) to the mumCfgInterConnection OID.', 'Added OID mumCfgCommitChange to the mumCfgTable.', 'Updated the description associated with the mumCfgCommitChange OID.', 'Updated the description associated with the mumCfgCommitChange OID again. Adjusted the copyright date and references to Paradyne.', 'New Release -- version 1.02.01',))
if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setLastUpdated('0411170200Z')
if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setOrganization('Paradyne Corporation')
if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setContactInfo('Paradyne Corporation 8545 126th Avenue North Largo, FL 33773 phone: +1 (727) 530 2000 email: support@paradyne.com www: http://www.nettonet.com/support/')
if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setDescription("This mib module defines an SNMP API to manage the Paradyne Corporation's DSLAM chassis parameters. These parameter settings are specifically associated with the the MUM200-2 and MUM2000-2 modules and the Mini and Micro DSLAMs. The interface types are described below, AMD8000-12 12-Port ADSL Mini DSLAMs With Full Rate and G.lite Operational Modes SMD2000-12, SMD2000Q-12, SMD2000G-12 12-Port SDSL Mini DSLAMs: AC and DC Versions with Cap, 2B1Q and G.SHDSL line encoding SuD2011_12T, SuD2011_12E, SuD2003_12T, SuD2003_12E 12-Port SDSL Micro DSLAMs: Cap, 2B1Q and G.SHDSL line encoding SuD2011_6T, SuD2011_6E, SuD2002_6T, SuD2002_6E 6-Port SDSL Micro DSLAMs: Cap, 2B1Q and G.SHDSL line encoding MUM200-2, MUM2000-2 Multiplexer Uplink Module with Dual Uplink Interface Module Capacity UIM-10/100 Uplink Interface Module UIM-DS3 DS3 Uplink Interface Module UIM-E1 E1 Uplink Interface Module UIM-E3 E3 Uplink Interface Module UIM-T1 T1 Uplink Interface Module ")
chsCfgMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1))
chsCfgParameterConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1))
prmCfgMultiplexerUplinkModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1))
mumCfgNotes = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 1), NtnDisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgNotes.setStatus('current')
if mibBuilder.loadTexts: mumCfgNotes.setDescription("The chassis system 'Notes' field is to be used as a scratchpad (i.e. chassis id or name) by the administrator. The default value is blank. The length of string must not exceed 128 alpha-numeric characters.")
mumCfgTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: mumCfgTable.setStatus('current')
if mibBuilder.loadTexts: mumCfgTable.setDescription('A list of MUM200-2/2000-2 module or Mini/Micro DSLAM entries.')
mumCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "mumCfgIndex"))
if mibBuilder.loadTexts: mumCfgEntry.setStatus('current')
if mibBuilder.loadTexts: mumCfgEntry.setDescription('An entry containing management information applicable to a MUM200-2/MUM2000-2 module or Mini/Micro DSLAM.')
mumCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumCfgIndex.setStatus('current')
if mibBuilder.loadTexts: mumCfgIndex.setDescription("Translates to the physical slot number that a MUM200-2/2000-2 module exists within a chassis. The Mini/Micro DSLAMs' physical location is set to 1 by default. See below, chassis type physical location(s) translation ------------ -------------------------------- IPD12000 MUM in slots 13,14 = mumCfgIndex 1,2 respecitively IPD4000 MUM in slot 5 = mumCfgIndex 1 Mini DSLAM NA = mumCfgIndex 1 Micro DSLAM NA = mumCfgIndex 1")
mumCfgIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgIpAddress.setStatus('current')
if mibBuilder.loadTexts: mumCfgIpAddress.setDescription('IP Address assigned to a MUM200-2/2000-2 module or Mini/Micro DSLAM. This parameter is initially set to a default value, i.e 192.168.254.252 for a MUM200-2/2000-2 module located in slot 13 of an IPD12000, slot 5 of an IPD4000 DSLAM and a Mini/Micro DSLAM. The default value of 192.168.254.253 will be for a MUM200-2/2000-2 module located in slot 14 of an IPD12000 (duplicate IP addresses are not allowed). These default values can be modified by the user.')
mumCfgSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgSubnetMask.setStatus('current')
if mibBuilder.loadTexts: mumCfgSubnetMask.setDescription('The Subnet Mask assigned to a MUM200-2/2000-2 module or Mini/Micro DSLAM. This parameter is assiged by the user, the default value is 255.255.255.0.')
mumCfgDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgDefaultGateway.setStatus('current')
if mibBuilder.loadTexts: mumCfgDefaultGateway.setDescription('The Default Gateway assigned to a MUM200-2/2000-2 module or Mini/Micro DSLAM. This value is assiged by the user, the default value is 0.0.0.0.')
mumCfgInbandMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgInbandMgmt.setStatus('current')
if mibBuilder.loadTexts: mumCfgInbandMgmt.setDescription('Inband management feature, when enabled [ON(1)], allows access to the DSLAM via the network against an assigned IP address, subnet mask, and default gateway.')
mumCfgInbandMGMTVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4085))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgInbandMGMTVlanID.setStatus('current')
if mibBuilder.loadTexts: mumCfgInbandMGMTVlanID.setDescription('The IP DSLAM supports 802.1Q Virtual LANs (VLANs). This parameter configuration applies to the inband management traffic only. It does not apply to out of band traffic received from the MGMT port. Note: for the case where the chassis type is an IPD12000 loaded with two MUMs, the setting of this parameter will affect both.')
mumCfgInterConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("neither", 1), ("uplink1", 2), ("uplink2", 3), ("uplink3", 4), ("uplink4", 5), ("mgmt", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgInterConnection.setStatus('current')
if mibBuilder.loadTexts: mumCfgInterConnection.setDescription('IPD12000 or IPD4000 DSLAM interconnect configuration provides the system manager the ability to daisy-chain one IP DSLAM to another so that a single router may be used for all DSLAMs in the chain.')
mumCfgCommitChange = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgCommitChange.setStatus('current')
if mibBuilder.loadTexts: mumCfgCommitChange.setDescription('Set to enabled(1) in order to commit the latest changes to the IP address, subnetmask, default gateway chassis parameters. This is only applicable to the SNE2040G-P and the SNE2040G-S.')
mumCfgUplinkInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3))
uimCfgEthTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: uimCfgEthTable.setStatus('current')
if mibBuilder.loadTexts: uimCfgEthTable.setDescription('A list of ethernet Uplink Interface Module (UIM) entries.')
uimCfgEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgEthMumIndex"), (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgEthIndex"))
if mibBuilder.loadTexts: uimCfgEthEntry.setStatus('current')
if mibBuilder.loadTexts: uimCfgEthEntry.setDescription('An entry containing information applicable to an ethernet Uplink Interface Module (UIM).')
uimCfgEthMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgEthMumIndex.setStatus('current')
if mibBuilder.loadTexts: uimCfgEthMumIndex.setDescription("Translates to the physical slot number that a MUM200-2/2000-2 module exists within a chassis. The Mini/Micro DSLAMs' physical location is set to 1 by default. See below, chassis type physical location(s) translation ------------ -------------------------------- IPD12000 MUM in slots 13,14 = uimCfgEthMumIndex 1,2 respecitively IPD4000 MUM in slot 5 = uimCfgEthMumIndex 1 Mini DSLAM NA = uimCfgEthMumIndex 1 Micro DSLAM NA = uimCfgEthMumIndex 1 Note: when configuring an ethernet UIM, the user must enter the index of the MUM, see above table, that corresponds with the IP address of the remote SNMP agent.")
uimCfgEthIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgEthIndex.setStatus('current')
if mibBuilder.loadTexts: uimCfgEthIndex.setDescription('The physical slot used to access the UIM in the MUM200-2/2000-2 module or Mini/Micro DSLAM.')
uimCfgEthRxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEth10", 1), ("uimEth100", 2), ("uimEthGig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgEthRxTxRate.setStatus('current')
if mibBuilder.loadTexts: uimCfgEthRxTxRate.setDescription('The RxTx rate for an ethernet UIM.')
uimCfgEthDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEthHalf", 1), ("uimEthFull", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgEthDuplex.setStatus('current')
if mibBuilder.loadTexts: uimCfgEthDuplex.setDescription('The current duplex setting for an ethernet UIM.')
uimCfgT1Table = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: uimCfgT1Table.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1Table.setDescription('A list of T1 Uplink Interface Module (UIM) entries.')
uimCfgT1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgT1MumIndex"), (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgT1Index"))
if mibBuilder.loadTexts: uimCfgT1Entry.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1Entry.setDescription('An entry containing information applicable to a T1 Uplink Interface Module (UIM).')
uimCfgT1MumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgT1MumIndex.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1MumIndex.setDescription("Translates to the physical slot number that a MUM200-2/2000-2 module exists within a chassis. The Mini/Micro DSLAMs' physical location is set to 1 by default. See below, chassis type physical location(s) translation ------------ -------------------------------- IPD12000 MUM in slots 13,14 = uimCfgT1MumIndex 1,2 respecitively IPD4000 MUM in slot 5 = uimCfgT1MumIndex 1 Mini DSLAM NA = uimCfgT1MumIndex 1 Micro DSLAM NA = uimCfgT1MumIndex 1 Note: when configuring a T1 UIM, the user must enter the index of the MUM, see above table, that corresponds with the IP address of the remote SNMP agent.")
uimCfgT1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgT1Index.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1Index.setDescription('The physical slot used to access the UIM in the MUM200-2/2000-2 module or Mini/Micro DSLAM.')
uimCfgT1Frame = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimT1ESF", 1), ("uimT1SFD4", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgT1Frame.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1Frame.setDescription('The frame type parameter for a T1 UIM.')
uimCfgT1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimT1B8ZS", 1), ("uimT1AMI", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgT1LineCode.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1LineCode.setDescription('The line code parameter for a T1 UIM.')
uimCfgT1LineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uimT10db", 1), ("uimT1N7p5db", 2), ("uimT1N15db", 3), ("uimT1N22p5db", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgT1LineBuildout.setStatus('current')
if mibBuilder.loadTexts: uimCfgT1LineBuildout.setDescription('The line buildout parameter for a T1 UIM.')
uimCfgE1Table = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3), )
if mibBuilder.loadTexts: uimCfgE1Table.setStatus('current')
if mibBuilder.loadTexts: uimCfgE1Table.setDescription('A list of E1 Uplink Interface Module (UIM) entries.')
uimCfgE1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgE1MumIndex"), (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgE1Index"))
if mibBuilder.loadTexts: uimCfgE1Entry.setStatus('current')
if mibBuilder.loadTexts: uimCfgE1Entry.setDescription('An entry containing information applicable to an E1 Uplink Interface Module (UIM).')
uimCfgE1MumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgE1MumIndex.setStatus('current')
if mibBuilder.loadTexts: uimCfgE1MumIndex.setDescription("Translates to the physical slot number that a MUM200-2/2000-2 module exists within a chassis. The Mini/Micro DSLAMs' physical location is set to 1 by default. See below, chassis type physical location(s) translation ------------ -------------------------------- IPD12000 MUM in slots 13,14 = uimCfgE1MumIndex 1,2 respecitively IPD4000 MUM in slot 5 = uimCfgE1MumIndex 1 Mini DSLAM NA = uimCfgE1MumIndex 1 Micro DSLAM NA = uimCfgE1MumIndex 1 Note: when configuring an E1 UIM, the user must enter the index of the MUM, see above table, that corresponds with the IP address of the remote SNMP agent.")
uimCfgE1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgE1Index.setStatus('current')
if mibBuilder.loadTexts: uimCfgE1Index.setDescription('The physical slot used to access the UIM in the MUM200-2/2000-2 module or Mini/Micro DSLAM.')
uimCfgE1Frame = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimE1CRC", 1), ("uimE1NoCRC", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgE1Frame.setStatus('current')
if mibBuilder.loadTexts: uimCfgE1Frame.setDescription('The frame type parameter for an E1 UIM.')
uimCfgE1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimE1HDB3", 1), ("uimE1AMI", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgE1LineCode.setStatus('current')
if mibBuilder.loadTexts: uimCfgE1LineCode.setDescription('The line code parameter for an E1 UIM.')
mumSNMPConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4))
snmpCfgNoticeIpTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1), )
if mibBuilder.loadTexts: snmpCfgNoticeIpTable.setStatus('current')
if mibBuilder.loadTexts: snmpCfgNoticeIpTable.setDescription('A list of SNMP trap notification Ip Addresses.')
snmpCfgNoticeIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "snmpCfgNoticeIndex"))
if mibBuilder.loadTexts: snmpCfgNoticeIpEntry.setStatus('current')
if mibBuilder.loadTexts: snmpCfgNoticeIpEntry.setDescription('An entry containing SNMP information applicable to a MUM200-2/MUM2000-2 module or Mini/Micro DSLAM.')
snmpCfgNoticeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpCfgNoticeIndex.setStatus('current')
if mibBuilder.loadTexts: snmpCfgNoticeIndex.setDescription('An integer value that points to one of four trap notification IP addresses.')
snmpCfgNoticeIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgNoticeIpAddress.setStatus('current')
if mibBuilder.loadTexts: snmpCfgNoticeIpAddress.setDescription('IP Address of the location or computer to which you would like trap notifications sent. The default value is 0.0.0.0 and it can be modified by the user.')
snmpCfgAuthenticationTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgAuthenticationTrapState.setStatus('current')
if mibBuilder.loadTexts: snmpCfgAuthenticationTrapState.setDescription('Indicates whether Authentication traps should be generated. By default, this object should have the value enabled(1).')
snmpCfgEnvironmentTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgEnvironmentTrapState.setStatus('current')
if mibBuilder.loadTexts: snmpCfgEnvironmentTrapState.setDescription('Indicates whether the fan and temperature traps should be generated. By default, this object should have the value enabled(1).')
snmpCfgColdstartTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgColdstartTrapState.setStatus('current')
if mibBuilder.loadTexts: snmpCfgColdstartTrapState.setDescription('Indicates whether Cold Start traps should be generated. By default, this object should have the value disabled(2).')
snmpCfgModulePortTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgModulePortTrapState.setStatus('current')
if mibBuilder.loadTexts: snmpCfgModulePortTrapState.setDescription('Indicates whether the module present/removed and link up/down traps should be generated. By default, this object should have the value disabled(2).')
snmpCfgCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6))
comReadWriteAccess = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comReadWriteAccess.setStatus('current')
if mibBuilder.loadTexts: comReadWriteAccess.setDescription('The community string that will allow the user read/write access to the agent. In otherwords, the user will be allowed to view and set parameter attributes. Note: since this is a hidden attribute, for security purposes, when performing a get on this OID the string that is returned will be represented by asterisk(s).')
comReadOnlyAccess = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comReadOnlyAccess.setStatus('current')
if mibBuilder.loadTexts: comReadOnlyAccess.setDescription('The community string that will allow the user read access to the agent. In otherwords, the user will be allowed to view parameter attributes. Note: since this is a hidden attribute, for security purposes, when performing a get on this OID the string that is returned will be represented by asterisk(s).')
mumCfgUniques = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 5))
unqEmbHttpWebsrvrState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unqEmbHttpWebsrvrState.setStatus('current')
if mibBuilder.loadTexts: unqEmbHttpWebsrvrState.setDescription('This configuration parameter allows the user the ability to disable, or enable, the embedded webserver. By default, this object should have the value enabled(1).')
mumCfgAdvanced = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6))
advCfgTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1), )
if mibBuilder.loadTexts: advCfgTable.setStatus('current')
if mibBuilder.loadTexts: advCfgTable.setDescription('A list of the Advanced Configuration entries.')
advCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "advCfgMumIndex"))
if mibBuilder.loadTexts: advCfgEntry.setStatus('current')
if mibBuilder.loadTexts: advCfgEntry.setDescription('An entry containing information applicable to an Advanced Configuration parameter.')
advCfgMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: advCfgMumIndex.setStatus('current')
if mibBuilder.loadTexts: advCfgMumIndex.setDescription("Translates to the physical slot number that a MUM200-2/2000-2 module exists within a chassis. The Mini/Micro DSLAMs' physical location is set to 1 by default. See below, chassis type physical location(s) translation ------------ -------------------------------- IPD12000 MUM in slots 13,14 = uimCfgE1MumIndex 1,2 respecitively IPD4000 MUM in slot 5 = uimCfgE1MumIndex 1 Mini DSLAM NA = uimCfgE1MumIndex 1 Micro DSLAM NA = uimCfgE1MumIndex 1 Note: when configuring an Advanced Configuration parameter, the user must enter the index of the MUM, see above table, that corresponds with the IP address of the remote SNMP agent.")
advCfgTFTPState = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgTFTPState.setStatus('current')
if mibBuilder.loadTexts: advCfgTFTPState.setDescription('This configuration parameter allows the user the ability to disable, or enable, the TFTP server. By default, this object should have the value enabled(1).')
advCfgTelnetState = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgTelnetState.setStatus('current')
if mibBuilder.loadTexts: advCfgTelnetState.setDescription('This configuration parameter allows the user the ability to disable, or enable, telnet. By default, this object should have the value enabled(1).')
advCfgMgmtFltrIpStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgMgmtFltrIpStart.setStatus('current')
if mibBuilder.loadTexts: advCfgMgmtFltrIpStart.setDescription("The start value for the management IP filter range. This parameter is initially set to a default filter range of 0.0.0.0 - 255.255.255.255. Connection to the management system will be allowed only if the user's Ip address value falls within the defined mumCfgMgmtIpStart and mumCfgMgmtIpEnd range.")
advCfgMgmtFltrIpEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgMgmtFltrIpEnd.setStatus('current')
if mibBuilder.loadTexts: advCfgMgmtFltrIpEnd.setDescription("The end value for the management IP filter range. This parameter is initially set to a default filter range of 0.0.0.0 - 255.255.255.255. Connection to the management system will be allowed only if the user's Ip address value falls within the defined mumCfgMgmtIpStart and mumCfgMgmtIpEnd range.")
advCfgMgmtSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 6), NtnTimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgMgmtSessionTimeout.setStatus('current')
if mibBuilder.loadTexts: advCfgMgmtSessionTimeout.setDescription('This value defines the length of a password session in seconds. If the session has been idle for a time greater than this value, the browser will be challenged again, even if it has provided authentication credentials with the request.')
mumCfgManagementPort = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7))
mgmtPortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1), )
if mibBuilder.loadTexts: mgmtPortCfgTable.setStatus('current')
if mibBuilder.loadTexts: mgmtPortCfgTable.setDescription('A list of the hardware platform management port entries.')
mgmtPortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "mgmtPortCfgMumIndex"))
if mibBuilder.loadTexts: mgmtPortCfgEntry.setStatus('current')
if mibBuilder.loadTexts: mgmtPortCfgEntry.setDescription('An entry containing information applicable to the managment (ethernet type) port.')
mgmtPortCfgMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmtPortCfgMumIndex.setStatus('current')
if mibBuilder.loadTexts: mgmtPortCfgMumIndex.setDescription("Translates to the physical slot number that a MUM200-2/2000-2 module exists within a chassis. The Mini/Micro DSLAMs' physical location is set to 1 by default. See below, chassis type physical location(s) translation ------------ -------------------------------- IPD12000 MUM in slots 13,14 = uimCfgEthMumIndex 1,2 respecitively IPD4000 MUM in slot 5 = uimCfgEthMumIndex 1 Mini DSLAM NA = uimCfgEthMumIndex 1 Micro DSLAM NA = uimCfgEthMumIndex 1 Note: when configuring a management port, the user must enter the index of the MUM, see above table, that corresponds with the IP address of the remote SNMP agent.")
mgmtPortCfgRxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEth10", 1), ("uimEth100", 2), ("uimEthGig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtPortCfgRxTxRate.setStatus('current')
if mibBuilder.loadTexts: mgmtPortCfgRxTxRate.setDescription('Set the RxTx rate for an ethernet management port.')
mgmtPortCfgDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEthHalf", 1), ("uimEthFull", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtPortCfgDuplex.setStatus('current')
if mibBuilder.loadTexts: mgmtPortCfgDuplex.setDescription('Set the duplex setting for an ethernet management port.')
mgmtPortCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgmt", 1), ("uplink", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtPortCfgType.setStatus('current')
if mibBuilder.loadTexts: mgmtPortCfgType.setDescription('Set the management port type as follows. By setting this port to mgmt(1), it will operate as a non-bridge mode connection. Setting it to uplink(2), this port will operate like an uplink interface module, i.e. a bridge mode connection. Note: this applies to the AuD8000-12 micro DSLAM only.')
mibBuilder.exportSymbols("NTNTECH-CHASSIS-CONFIGURATION-MIB", uimCfgE1Index=uimCfgE1Index, uimCfgT1Frame=uimCfgT1Frame, snmpCfgNoticeIpAddress=snmpCfgNoticeIpAddress, mgmtPortCfgEntry=mgmtPortCfgEntry, snmpCfgNoticeIndex=snmpCfgNoticeIndex, chsCfgMIBObjects=chsCfgMIBObjects, advCfgTelnetState=advCfgTelnetState, mgmtPortCfgDuplex=mgmtPortCfgDuplex, mumCfgUplinkInterfaceModule=mumCfgUplinkInterfaceModule, mgmtPortCfgType=mgmtPortCfgType, advCfgTFTPState=advCfgTFTPState, mumCfgNotes=mumCfgNotes, uimCfgEthIndex=uimCfgEthIndex, snmpCfgAuthenticationTrapState=snmpCfgAuthenticationTrapState, mgmtPortCfgRxTxRate=mgmtPortCfgRxTxRate, mumCfgIpAddress=mumCfgIpAddress, uimCfgE1LineCode=uimCfgE1LineCode, snmpCfgNoticeIpEntry=snmpCfgNoticeIpEntry, PYSNMP_MODULE_ID=ntntechChassisConfigurationMIB, uimCfgEthTable=uimCfgEthTable, uimCfgE1Table=uimCfgE1Table, uimCfgT1Index=uimCfgT1Index, snmpCfgNoticeIpTable=snmpCfgNoticeIpTable, snmpCfgCommunity=snmpCfgCommunity, mumCfgSubnetMask=mumCfgSubnetMask, uimCfgT1Entry=uimCfgT1Entry, mgmtPortCfgTable=mgmtPortCfgTable, mgmtPortCfgMumIndex=mgmtPortCfgMumIndex, mumCfgTable=mumCfgTable, mumCfgAdvanced=mumCfgAdvanced, uimCfgE1MumIndex=uimCfgE1MumIndex, uimCfgE1Entry=uimCfgE1Entry, unqEmbHttpWebsrvrState=unqEmbHttpWebsrvrState, mumCfgEntry=mumCfgEntry, uimCfgEthMumIndex=uimCfgEthMumIndex, mumCfgCommitChange=mumCfgCommitChange, snmpCfgModulePortTrapState=snmpCfgModulePortTrapState, advCfgTable=advCfgTable, mumCfgInterConnection=mumCfgInterConnection, uimCfgEthEntry=uimCfgEthEntry, comReadWriteAccess=comReadWriteAccess, uimCfgEthDuplex=uimCfgEthDuplex, snmpCfgEnvironmentTrapState=snmpCfgEnvironmentTrapState, snmpCfgColdstartTrapState=snmpCfgColdstartTrapState, mumSNMPConfiguration=mumSNMPConfiguration, ntntechChassisConfigurationMIB=ntntechChassisConfigurationMIB, uimCfgT1LineBuildout=uimCfgT1LineBuildout, uimCfgT1Table=uimCfgT1Table, chsCfgParameterConfiguration=chsCfgParameterConfiguration, comReadOnlyAccess=comReadOnlyAccess, mumCfgIndex=mumCfgIndex, uimCfgT1LineCode=uimCfgT1LineCode, advCfgEntry=advCfgEntry, advCfgMumIndex=advCfgMumIndex, advCfgMgmtSessionTimeout=advCfgMgmtSessionTimeout, mumCfgDefaultGateway=mumCfgDefaultGateway, mumCfgInbandMgmt=mumCfgInbandMgmt, mumCfgUniques=mumCfgUniques, mumCfgManagementPort=mumCfgManagementPort, uimCfgT1MumIndex=uimCfgT1MumIndex, uimCfgE1Frame=uimCfgE1Frame, mumCfgInbandMGMTVlanID=mumCfgInbandMGMTVlanID, advCfgMgmtFltrIpEnd=advCfgMgmtFltrIpEnd, prmCfgMultiplexerUplinkModule=prmCfgMultiplexerUplinkModule, advCfgMgmtFltrIpStart=advCfgMgmtFltrIpStart, uimCfgEthRxTxRate=uimCfgEthRxTxRate)
