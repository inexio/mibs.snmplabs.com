#
# PySNMP MIB module ERI-DNX-OCTAL-T1E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-OCTAL-T1E1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
LinkPortAddress, PortStatus, devices, trapSequence, FunctionSwitch, LinkCmdStatus, OneByteField, DataSwitch, DecisionType = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "LinkPortAddress", "PortStatus", "devices", "trapSequence", "FunctionSwitch", "LinkCmdStatus", "OneByteField", "DataSwitch", "DecisionType")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Bits, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, NotificationType, Gauge32, iso, Counter64, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Bits", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "NotificationType", "Gauge32", "iso", "Counter64", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriDNXOctalT1E1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 2))
if mibBuilder.loadTexts: eriDNXOctalT1E1MIB.setLastUpdated('200203080000Z')
if mibBuilder.loadTexts: eriDNXOctalT1E1MIB.setOrganization('Eastern Research, Inc.')
if mibBuilder.loadTexts: eriDNXOctalT1E1MIB.setContactInfo('Customer Service Postal: Eastern Research, Inc. 225 Executive Drive Moorestown, NJ 08057 Phone: +1-800-337-4374 Email: support@erinc.com')
if mibBuilder.loadTexts: eriDNXOctalT1E1MIB.setDescription('The ERI Enterprise MIB Module for the DNX T1/E1 ports.')
dnxOT1E1 = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4))
oteConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1))
oteDiag = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 2))
oT1E1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1), )
if mibBuilder.loadTexts: oT1E1ConfigTable.setStatus('current')
if mibBuilder.loadTexts: oT1E1ConfigTable.setDescription("This is the Octal T1/E1 Configuration table which consists of an entry for each of the Octal T1/E1 card's 8 links(ports). The total number of entries depends on the number of Octal T1/E1 cards in the nest. Changes to the Link Configuration must be made on a record or row by row basis. This means that any use of the Set command on writable fields must include the oT1E1CfgCmdStatus field with a value of 'update' as the last variable in the SET PDU.")
oT1E1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-OCTAL-T1E1-MIB", "oT1E1CfgLinkAddr"))
if mibBuilder.loadTexts: oT1E1ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oT1E1ConfigEntry.setDescription("The conceptual row of the Octal T1/E1 Configuration table. A row in this table cannot be added or deleted, only modified using the oT1E1CfgCmdStatus field with a value of 'update' as the last variable in the SET PDU. The oT1E1CfgCmdStatus field must be included as the last variable in a SET PDU for the action to take effect. If the oT1E1CfgCmdStatus is missing from the SET PDU, the GET RESPONSE will contain the SNMP error status of 'genErr' for and an error index equal to the last variable.")
oT1E1CfgLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oT1E1CfgLinkAddr.setStatus('current')
if mibBuilder.loadTexts: oT1E1CfgLinkAddr.setDescription('This number uniquely identifies an Octal T1/E1 link resource. This number will be used throughout the system to identify a unique link. The format is represented using an IP address syntax (4 byte string). Note that the maximum valid port number will vary depending on the specified carrier and framing options. For example, an octal T1/E1 device has 8 ports but the DS3 has 28 ports. The 1st byte is reserved for future Nest Number use The 2nd byte represents the Slot Number (1-11) The 3rd byte represents the Port Number (1-32) The 4th byte is reserved for future use ')
oT1E1CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oT1E1CfgResource.setStatus('current')
if mibBuilder.loadTexts: oT1E1CfgResource.setDescription('Uniquely identifies an Octal T1/E1 link in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
oT1E1CfgLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1CfgLinkName.setStatus('current')
if mibBuilder.loadTexts: oT1E1CfgLinkName.setDescription('This is the user friendly text name to identify the link.')
oT1E1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 4), PortStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1Status.setStatus('current')
if mibBuilder.loadTexts: oT1E1Status.setDescription('Dictates the current status of the port, in-service or out-of-service.')
oT1E1ClearT1E1 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("framed", 1), ("unframed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1ClearT1E1.setStatus('current')
if mibBuilder.loadTexts: oT1E1ClearT1E1.setDescription('Determines if the port supports T1 or E1 unframed.')
oT1E1LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13))).clone(namedValues=NamedValues(("e1", 0), ("e1-crc", 1), ("e1-cas", 2), ("e1-cas-crc", 3), ("e1-unframed", 4), ("t1-esf-b8zs", 5), ("t1-esf-ami-62411", 6), ("t1-d4-b8zs", 7), ("t1-d4-ami-62411", 8), ("t1-b8zs-unframed", 10), ("t1-ami-unframed", 11), ("t1-d4-ami-clear", 12), ("t1-esf-ami-clear", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1LineType.setStatus('current')
if mibBuilder.loadTexts: oT1E1LineType.setDescription('Determines the type of framing used on the line. Choose between E1 (Europeon) or T1 type framing options. When value of oT1E1ClearT1E1 is set to unframed (2), the only valid framing options are: e1-unframed (5) t1-b8zs-unframed (10) t1-ami-unframed (11) ')
oT1E1NetLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 7), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1NetLoop.setStatus('current')
if mibBuilder.loadTexts: oT1E1NetLoop.setDescription("Determines whether or not the module should respond to loop diagnostic commands received from the network supplier. Select 'enable' unless the commands are to be passed to another T1/E1 device.")
oT1E1YelAlrm = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 8), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1YelAlrm.setStatus('current')
if mibBuilder.loadTexts: oT1E1YelAlrm.setDescription("Causes the module to discard data and send a yellow alarm if it is in a red alarm condition after the set recover time period. 'Yes' must be chosen if the network supplier is a common carrier, such as a telephone company.")
oT1E1RecoverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 10, 15))).clone(namedValues=NamedValues(("timeout-3-secs", 3), ("timeout-10-secs", 10), ("timeout-15-secs", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1RecoverTime.setStatus('current')
if mibBuilder.loadTexts: oT1E1RecoverTime.setDescription('This is the red alarm timeout value. Determines the amount of seconds the port will wait to stop sending the yellow alarm when coming out of a red alarm condition. This field does not apply to E1 links.')
oT1E1IdleCode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("busy", 0), ("idle", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1IdleCode.setStatus('current')
if mibBuilder.loadTexts: oT1E1IdleCode.setDescription("Determines the whether the data that will be transmitted over the unused Ds0s will be 'idle' or 'busy' (all 1's).")
oT1E1EsfFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("att-54016", 1), ("ansi-t1-403", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1EsfFormat.setStatus('current')
if mibBuilder.loadTexts: oT1E1EsfFormat.setDescription('Determines the type of ESF network commands the T-1 link will respond to. It has no meaning for D4 networks. With ESF networks, this information must be obtained from the network supplier. ESF does not apply to E1 links.')
oT1E1CfgLBO = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("e1-shortHaul-0-6db", 1), ("e1-longHaul-0-34db", 2), ("t1-longHaul-0-0db", 3), ("t1-longHaul-7-5db", 4), ("t1-longHaul-15-0db", 5), ("t1-longHaul-22-5db", 6), ("t1-shortHaul-0-133ft", 7), ("t1-shortHaul-133-266ft", 8), ("t1-shortHaul-266-399ft", 9), ("t1-shortHaul-399-533ft", 10), ("t1-shortHaul-533-655ft", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1CfgLBO.setStatus('current')
if mibBuilder.loadTexts: oT1E1CfgLBO.setDescription('Determines the type of Line Build Out (LBO) used on the link. Choose between short haul or long haul designations but this varies between T1 & E1. E1 LBO is defined by authentication of signal presented to receiving circuitry while T1 LBO can be defined by cable length or signal. e1-shortHaul-0-6db (1) 0 to -6 decibel loss e1-longHaul-0-34db (2) 0 to -34 decibel loss t1-longHaul-0-0db (3) 0.0 decibel loss t1-longHaul-7-5db (4) 0.0 to -7.5 decibel loss t1-longHaul-15-0db (5) 0.0 to -15.0 decibel loss t1-longHaul-22-5db (6) 0.0 to -22.5 decibel loss t1-shortHaul-0-133ft (7) 0 to 133 feet of cable t1-shortHaul-133-266ft (8) 133 to 266 feet of cable t1-shortHaul-266-399ft (9) 266 to 399 feet of cable t1-shortHaul-399-533ft (10) 399 to 533 feet of cable t1-shortHaul-533-655ft (11) 533 to 655 feet of cable')
oT1E1CfgCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 13), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1CfgCmdStatus.setStatus('current')
if mibBuilder.loadTexts: oT1E1CfgCmdStatus.setDescription("The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row T1/E1 Link Commands used in SET Command (1..99) update-link-config(1) Change existing Link Configuration inServiceAll (7) Change Link Status to in-service for all 8 links. copyToAll (9) Copy T1 Link configuration to all other links within the same device outOfServiceAll (12) Change Link Status to out-of-service for all 8 links. Response States used in GET RESPONSE Command (100..199) update-successful (101) Link data has been successfully changed insvc-successful (107) All Links have been successfully placed In Service copy-successful (109) T1 Link data has been successfully copied to other links oos-successful (112) All Links have been successfully placed Out of Service T1/E1 Link Config Error Codes used in GET RESPONSE Command (200..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-status (401) Unrecognized link status setting err-invalid-link-framing (402) Line framing type not valid for link type err-invalid-link-command (403) Unrecognized link command-action err-invalid-link-lbo (404) Line Build Out option not valid for link type err-invalid-esf-format (405) ESF type not applicable to link type err-invalid-network-loop (410) Unrecognized network loop setting err-invalid-yellow-alrm (411) Unrecognized yellow alarm setting err-invalid-red-timeout (412) Unrecognized red alarm timeout err-invalid-idle-code (413) Unrecognized idle code err-device-in-standby (414) Can't change config for designated Standby device err-invalid-link-bits (427) Reserved E1 National bits must be left at zero. err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big")
oT1E1Gr303Facility = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 14), DecisionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oT1E1Gr303Facility.setStatus('obsolete')
if mibBuilder.loadTexts: oT1E1Gr303Facility.setDescription('Enables link to be configured as a Gr303 Facility')
oT1E1NationalBits = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 15), OneByteField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1NationalBits.setStatus('current')
if mibBuilder.loadTexts: oT1E1NationalBits.setDescription('Enables E1 National S-bits to be set to zero or one. This single byte field can be changed to set the values of the E1 NFA byte in odd frames as depicted below: sa8 sa7 sa6 sa5 sa4 reserved bits --- --- --- --- --- ------------- 1 1 1 1 1 0 0 0 = F8 (default) Values should be entered in Hex. If reserved bits are changed, an error code (427) will be returned in the command status. ')
oT1E1InterNational = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 1, 1, 1, 16), OneByteField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oT1E1InterNational.setStatus('current')
if mibBuilder.loadTexts: oT1E1InterNational.setDescription('Enables InterNational S(i) Spare bit to be set to zero or one. This single byte field can be changed to set the values of the Bit 1 of TS0 G.704 frame as depicted below: reserved bits S(i) -------------------------- ----- 0 0 0 0 0 0 0 1 = 01 (default) Values should be entered in Hex. If reserved bits are changed, an error code (427) will be returned in the command status. ')
dnxOT1E1Enterprise = ObjectIdentity((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 0))
if mibBuilder.loadTexts: dnxOT1E1Enterprise.setStatus('current')
if mibBuilder.loadTexts: dnxOT1E1Enterprise.setDescription('ERI DNX T1/E1 Enterprise for Alarms/Events')
oT1E1ConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 4, 0, 1)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-OCTAL-T1E1-MIB", "oT1E1CfgLinkAddr"), ("ERI-DNX-OCTAL-T1E1-MIB", "oT1E1CfgCmdStatus"))
if mibBuilder.loadTexts: oT1E1ConfigTrap.setStatus('current')
if mibBuilder.loadTexts: oT1E1ConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the configuration for specific T1/E1 Port.')
mibBuilder.exportSymbols("ERI-DNX-OCTAL-T1E1-MIB", oT1E1InterNational=oT1E1InterNational, oT1E1CfgLBO=oT1E1CfgLBO, oteDiag=oteDiag, oT1E1ConfigTrap=oT1E1ConfigTrap, oT1E1ConfigEntry=oT1E1ConfigEntry, oT1E1NetLoop=oT1E1NetLoop, oT1E1ClearT1E1=oT1E1ClearT1E1, oT1E1RecoverTime=oT1E1RecoverTime, dnxOT1E1=dnxOT1E1, oT1E1EsfFormat=oT1E1EsfFormat, oT1E1LineType=oT1E1LineType, oT1E1YelAlrm=oT1E1YelAlrm, eriDNXOctalT1E1MIB=eriDNXOctalT1E1MIB, oT1E1CfgCmdStatus=oT1E1CfgCmdStatus, oT1E1CfgResource=oT1E1CfgResource, oT1E1ConfigTable=oT1E1ConfigTable, oT1E1CfgLinkAddr=oT1E1CfgLinkAddr, dnxOT1E1Enterprise=dnxOT1E1Enterprise, oteConfig=oteConfig, oT1E1Gr303Facility=oT1E1Gr303Facility, oT1E1CfgLinkName=oT1E1CfgLinkName, oT1E1IdleCode=oT1E1IdleCode, oT1E1Status=oT1E1Status, oT1E1NationalBits=oT1E1NationalBits, PYSNMP_MODULE_ID=eriDNXOctalT1E1MIB)
