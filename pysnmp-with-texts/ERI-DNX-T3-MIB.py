#
# PySNMP MIB module ERI-DNX-T3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-T3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
trapSequence, DecisionType, FunctionSwitch, LinkCmdStatus, dnx, devices, PortStatus, LinkPortAddress = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "trapSequence", "DecisionType", "FunctionSwitch", "LinkCmdStatus", "dnx", "devices", "PortStatus", "LinkPortAddress")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, ObjectIdentity, Counter64, iso, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "ObjectIdentity", "Counter64", "iso", "Unsigned32", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriDNXT3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 3))
eriDNXT3MIB.setRevisions(('2002-08-19 00:00', '2002-04-11 00:00', '2001-04-01 00:00', '2000-09-15 00:00', '2000-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eriDNXT3MIB.setRevisionsDescriptions(('Nevio Poljak - eri_DnxNest MIB Rev 01.0 Fixed OID for this module indentity to avoid conflict with the LinkTest MIB module.', 'Nevio Poljak for Release 14.2 Converted to SMIv2 format.', 'Nevio Poljak - Release 12.0 Added new InService-OOS commands for all links.', 'Nevio Poljak Redefined Traps to use enterprise from their own MIB modules', 'Nevio Poljak Draft Release',))
if mibBuilder.loadTexts: eriDNXT3MIB.setLastUpdated('200208190000Z')
if mibBuilder.loadTexts: eriDNXT3MIB.setOrganization('Eastern Research, Inc.')
if mibBuilder.loadTexts: eriDNXT3MIB.setContactInfo('Customer Service Postal: Eastern Research, Inc. 225 Executive Drive Moorestown, NJ 08057 Phone: +1-800-337-4374 Email: support@erinc.com')
if mibBuilder.loadTexts: eriDNXT3MIB.setDescription('The ERI Enterprise MIB Module for the DNX T3 Device.')
dnxT3 = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1))
t3Config = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1))
t3Diag = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 2))
t3PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1), )
if mibBuilder.loadTexts: t3PortConfigTable.setStatus('current')
if mibBuilder.loadTexts: t3PortConfigTable.setDescription('This is the T3 Port Configuration table which consists of an entry for each of the T3 cards. The total number of entries depends on the number of T3 cards in the nest.')
t3PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-T3-MIB", "t3CfgAddr"))
if mibBuilder.loadTexts: t3PortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: t3PortConfigEntry.setDescription('The conceptual row of the T3 Port Configuration table. A row in this table cannot be added or deleted, only modified.')
t3CfgAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3CfgAddr.setStatus('current')
if mibBuilder.loadTexts: t3CfgAddr.setDescription('This number uniquely identifies a T3 slot/port.')
t3CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3CfgResource.setStatus('current')
if mibBuilder.loadTexts: t3CfgResource.setDescription('Uniquely identifies an T3 Port in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
t3CfgCircuitName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3CfgCircuitName.setStatus('current')
if mibBuilder.loadTexts: t3CfgCircuitName.setDescription('This is the user friendly text name to identify the circuit.')
t3FacilityId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3FacilityId.setStatus('current')
if mibBuilder.loadTexts: t3FacilityId.setDescription('This is a description of the facility where this equipment is located.')
t3EquipmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3EquipmentId.setStatus('current')
if mibBuilder.loadTexts: t3EquipmentId.setDescription('This is a description of the equipment in use.')
t3Location = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3Location.setStatus('current')
if mibBuilder.loadTexts: t3Location.setDescription('This is the user description of the location for this equipment.')
t3FrameId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3FrameId.setStatus('current')
if mibBuilder.loadTexts: t3FrameId.setDescription('This is the description of the building where this equipment is located.')
t3UnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3UnitName.setStatus('current')
if mibBuilder.loadTexts: t3UnitName.setDescription('This is the description of the bay or device this equipment is part of.')
t3PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3PortNumber.setStatus('current')
if mibBuilder.loadTexts: t3PortNumber.setDescription('This is the user description of the DS3 port.')
t3Generator = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3Generator.setStatus('current')
if mibBuilder.loadTexts: t3Generator.setDescription('This is the user description of the number generated by this equipment.')
t3M13OpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("c-bit", 0), ("bellcoreM13", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3M13OpMode.setStatus('current')
if mibBuilder.loadTexts: t3M13OpMode.setDescription('The framing selection for the DS1 to DS3 multiplexing.')
t3RcvLoopTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 12), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3RcvLoopTiming.setStatus('current')
if mibBuilder.loadTexts: t3RcvLoopTiming.setDescription('Enables or disables the DS3 transmit timing provided by the receive clock. When disabled, timing is provided by an on-board oscillator.')
t3ShortCable = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 13), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3ShortCable.setStatus('current')
if mibBuilder.loadTexts: t3ShortCable.setDescription("Indicates the line build out of the DS3 transmitter. 'Yes' when attached to a cable less than 50 feet long.")
t3M13RemLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("third-cbit-inverted", 0), ("second-cbit-inverted", 1), ("first-cbit-inverted", 2), ("third-cbit-stuffbit-inverted", 4), ("second-cbit-stuffbit-inverted", 5), ("first-cbit-stuffbit-inverted", 6), ("stuffbit-inverted", 7), ("stuffbit-is-zero", 8), ("stuffbit-is-one", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3M13RemLoop.setStatus('current')
if mibBuilder.loadTexts: t3M13RemLoop.setDescription('Controls the line codes used to set and reset DS1 remote line loopback requests. This applies the BellCore M13 mode only.')
t3RcvAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("framed1010-Cbit0-noXbit", 0), ("framed1010-Cbit0-Xbit1", 1), ("framed1010-noCbit-noXbit", 2), ("framed1111-noCbit-noXbit", 3), ("unframed1010", 4), ("unframed-allones", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3RcvAIS.setStatus('current')
if mibBuilder.loadTexts: t3RcvAIS.setDescription('The Received bit pattern that will cause an error.')
t3XmtAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ansi", 0), ("framed-allones-Cbit1", 1), ("unframed1010", 2), ("unframed-allones", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3XmtAIS.setStatus('current')
if mibBuilder.loadTexts: t3XmtAIS.setDescription('The Transmitted bit pattern that will cause an error.')
t3CmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 1, 1, 17), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3CmdStatus.setStatus('current')
if mibBuilder.loadTexts: t3CmdStatus.setDescription('The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row T3 Link Commands used in SET Command (1..99) update-link-config(1), Change existing Link Configuration Response States used in GET RESPONSE Command (100..199) update-successful (101) Link data has been successfully changed T3 Port Config Error Codes used in GET RESPONSE Command (100..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-status (401) Unrecognized link status setting err-invalid-link-framing (402) Line framing type not valid for link type err-invalid-link-command (403) Unrecognized link command-action err-invalid-link-op-mode (407) Configured M13 Op mode not valid for port; verify other link parameters match desired new mode err-invalid-link-rem-loop (408) Remote Loop type not valid for t3 frame type err-invalid-link-ais (409) Unrecognized t3 AIS selection err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
t3T1LinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2), )
if mibBuilder.loadTexts: t3T1LinkConfigTable.setStatus('current')
if mibBuilder.loadTexts: t3T1LinkConfigTable.setDescription("This is the T3 T-1 Link Configuration table which consists of an entry for each of the card's 28 links. The total number of entries depends on the number of DS3 cards in the nest.")
t3T1LinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1), ).setIndexNames((0, "ERI-DNX-T3-MIB", "t3T1CfgLinkAddr"))
if mibBuilder.loadTexts: t3T1LinkConfigEntry.setStatus('current')
if mibBuilder.loadTexts: t3T1LinkConfigEntry.setDescription('The conceptual row of the T3 T-1 Link Configuration table. A row in this table cannot be added or deleted, only modified.')
t3T1CfgLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3T1CfgLinkAddr.setStatus('current')
if mibBuilder.loadTexts: t3T1CfgLinkAddr.setDescription('This number uniquely identifies a T3/T-1 link resource. This number will be used throughout the system to identify a unique resource.')
t3T1CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t3T1CfgResource.setStatus('current')
if mibBuilder.loadTexts: t3T1CfgResource.setDescription('Uniquely identifies an T3 T1 Channel in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
t3T1CfgLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1CfgLinkName.setStatus('current')
if mibBuilder.loadTexts: t3T1CfgLinkName.setDescription('This is the user friendly text name to identify the link.')
t3T1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 4), PortStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1Status.setStatus('current')
if mibBuilder.loadTexts: t3T1Status.setDescription('Dictates the current status of the link, in-service or out-of-service.')
t3T1Framing = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("d4", 1), ("esf", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1Framing.setStatus('current')
if mibBuilder.loadTexts: t3T1Framing.setDescription("Determines the type of framing used on the line. Choose between SuperFrame 'D4' or Extended SuperFrame (ESF).")
t3T1Density = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("clear", 0), ("att-62411", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1Density.setStatus('current')
if mibBuilder.loadTexts: t3T1Density.setDescription("Determines the type of network signal used on the link. If line code is B8ZS, choose 'clear'. If line code is AMI, choose 62411.")
t3T1NetLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 7), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1NetLoop.setStatus('current')
if mibBuilder.loadTexts: t3T1NetLoop.setDescription("Determines whether or not the module should respond to loop diagnostic commands received from the network supplier. Select 'enable' unless the commands are to be passed to another DS3 device.")
t3T1YelAlrm = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 8), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1YelAlrm.setStatus('current')
if mibBuilder.loadTexts: t3T1YelAlrm.setDescription("Causes the module to discard data and send a yellow alarm if it is in a red alarm condition after a 3 second period. 'Yes' must be chosen if the network supplier is a common carrier, such as a telephone company.")
t3T1RecoverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 10, 15))).clone(namedValues=NamedValues(("timeout-3-secs", 3), ("timeout-10-secs", 10), ("timeout-15-secs", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1RecoverTime.setStatus('current')
if mibBuilder.loadTexts: t3T1RecoverTime.setDescription('This is the red alarm timeout value. Determines the amount of seconds the port will wait to stop sending the yellow alarm when coming out of a red alarm condition.')
t3T1EsfFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("att-54016", 0), ("ansi-t1-403", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1EsfFormat.setStatus('current')
if mibBuilder.loadTexts: t3T1EsfFormat.setDescription('Determines the type of ESF network commands the T-1 link will respond to. It has no meaning for D4 networks. With ESF networks, this information must be obtained from the network supplier.')
t3T1IdleCode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("busy", 0), ("idle", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1IdleCode.setStatus('current')
if mibBuilder.loadTexts: t3T1IdleCode.setDescription("Determines the whether the code that will be transmitted over the unused links will be 'idle' or 'busy' (all 1's).")
t3T1CfgCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 1, 2, 1, 12), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t3T1CfgCmdStatus.setStatus('current')
if mibBuilder.loadTexts: t3T1CfgCmdStatus.setDescription("The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row T3-T1 Link Commands used in SET Command (1..99) update-link-config(1) Change existing Link Configuration inServiceAll (7) Change Link Status to in-service for all 8 links. copyToAll (9) Copy T1 Link configuration to all other links within the same device outOfServiceAll (12) Change Link Status to out-of-service for all 8 links. Response States used in GET RESPONSE Command (100..199) update-successful (101) Link data has been successfully changed insvc-successful (107) All Links have been successfully placed In Service copy-successful (109) T1 Link data has been successfully copied to other links oos-successful (112) All Links have been successfully placed Out of Service T3-T1 Link Config Error Codes used in GET RESPONSE Command (200..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-status (401) Unrecognized link status setting err-invalid-link-framing (402) Line framing type not valid for link type err-invalid-link-command (403) Unrecognized link command-action err-invalid-esf-format (405) ESF type not applicable to link type err-invalid-link-density (406) Unrecognized T1 link density setting err-invalid-network-loop (410) Unrecognized network loop setting err-invalid-yellow-alrm (411) Unrecognized yellow alarm setting err-invalid-red-timeout (412) Unrecognized red alarm timeout err-invalid-idle-code (413) Unrecognized idle code err-device-in-standby (414) Can't change config for designated Standby device err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big")
dnxT3Enterprise = ObjectIdentity((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0))
if mibBuilder.loadTexts: dnxT3Enterprise.setStatus('current')
if mibBuilder.loadTexts: dnxT3Enterprise.setDescription('ERI DNX T3 Enterprise for Alarms/Events')
t3PortConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0, 1)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-T3-MIB", "t3CfgAddr"), ("ERI-DNX-T3-MIB", "t3CmdStatus"))
if mibBuilder.loadTexts: t3PortConfigTrap.setStatus('current')
if mibBuilder.loadTexts: t3PortConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the configuration for a given T3 Port entry.')
t3T1ConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 1, 0, 2)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-T3-MIB", "t3T1CfgLinkAddr"), ("ERI-DNX-T3-MIB", "t3T1CfgCmdStatus"))
if mibBuilder.loadTexts: t3T1ConfigTrap.setStatus('current')
if mibBuilder.loadTexts: t3T1ConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the Link configuration for a given T3-T1 channel entry.')
mibBuilder.exportSymbols("ERI-DNX-T3-MIB", t3T1LinkConfigEntry=t3T1LinkConfigEntry, t3T1CfgLinkName=t3T1CfgLinkName, eriDNXT3MIB=eriDNXT3MIB, t3M13RemLoop=t3M13RemLoop, t3RcvLoopTiming=t3RcvLoopTiming, t3PortConfigEntry=t3PortConfigEntry, t3RcvAIS=t3RcvAIS, t3PortNumber=t3PortNumber, t3T1NetLoop=t3T1NetLoop, t3Generator=t3Generator, t3T1LinkConfigTable=t3T1LinkConfigTable, t3CfgAddr=t3CfgAddr, t3T1ConfigTrap=t3T1ConfigTrap, t3PortConfigTable=t3PortConfigTable, t3T1Density=t3T1Density, t3T1YelAlrm=t3T1YelAlrm, dnxT3=dnxT3, t3T1RecoverTime=t3T1RecoverTime, t3CfgCircuitName=t3CfgCircuitName, t3T1Status=t3T1Status, t3CfgResource=t3CfgResource, t3UnitName=t3UnitName, t3T1CfgResource=t3T1CfgResource, dnxT3Enterprise=dnxT3Enterprise, t3EquipmentId=t3EquipmentId, t3Config=t3Config, t3CmdStatus=t3CmdStatus, PYSNMP_MODULE_ID=eriDNXT3MIB, t3Location=t3Location, t3T1CfgLinkAddr=t3T1CfgLinkAddr, t3FacilityId=t3FacilityId, t3T1Framing=t3T1Framing, t3T1EsfFormat=t3T1EsfFormat, t3Diag=t3Diag, t3T1CfgCmdStatus=t3T1CfgCmdStatus, t3M13OpMode=t3M13OpMode, t3ShortCable=t3ShortCable, t3T1IdleCode=t3T1IdleCode, t3FrameId=t3FrameId, t3PortConfigTrap=t3PortConfigTrap, t3XmtAIS=t3XmtAIS)
