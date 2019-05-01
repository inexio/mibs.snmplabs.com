#
# PySNMP MIB module PANDATEL-FME-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-FME-MODEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:37:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
device_id, mdmSpecifics = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "device-id", "mdmSpecifics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, ModuleIdentity, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, Counter64, NotificationType, Integer32, Gauge32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "Counter64", "NotificationType", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fme_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 601)).setLabel("fme-modem")
fme = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601))
fmeModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1), )
if mibBuilder.loadTexts: fmeModemTable.setStatus('mandatory')
if mibBuilder.loadTexts: fmeModemTable.setDescription('This table contains information about all FME units within all stacks.')
fmeTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1), ).setIndexNames((0, "PANDATEL-FME-MODEM-MIB", "mdmRack"), (0, "PANDATEL-FME-MODEM-MIB", "mdmModem"), (0, "PANDATEL-FME-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: fmeTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fmeTableEntry.setDescription('The index of the table.')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
if mibBuilder.loadTexts: mdmRack.setDescription('The index of the stack the unit belongs to. The stack corresponds to a rack, the FME units correspond to rack mount cards installed in a rack.')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
if mibBuilder.loadTexts: mdmModem.setDescription('This entry displays the index of the FME unit. It corresponds with its position in the stack.')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
if mibBuilder.loadTexts: mdmPosition.setDescription("This entry displays the location of the corresponding unit: 'local' or 'remote'. The unit which belongs to a managed stack is 'local', the counterpart is 'remote'.")
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
if mibBuilder.loadTexts: mdmModemName.setDescription('The verbal name of this unit.')
mdmActiveLink = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(7, 8, 90))).clone(namedValues=NamedValues(("line-port-7", 7), ("line-port-8", 8), ("disable", 90)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmActiveLink.setStatus('mandatory')
if mibBuilder.loadTexts: mdmActiveLink.setDescription('This entry displays the line port that is receiving data.')
mdmAlarmConditionPort7 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 116), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("no-link-signal", 3), ("laser-fail", 4), ("no-link-signal-or-laser-fail", 5), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmAlarmConditionPort7.setStatus('mandatory')
if mibBuilder.loadTexts: mdmAlarmConditionPort7.setDescription("The alarm trigger mode at port 7: 'disable', i.e. no alarm is triggered, 'no-link-signal', i.e. an alarm is triggered if the link is down, 'laser-fail', i.e. an alarm is triggered if the laser diode is defective, or 'no-link-signal-or-laser-fail', i.e. the link is down or the laser diode is defective.")
mdmAlarmConditionPort8 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 1, 1, 117), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("no-link-signal", 3), ("laser-fail", 4), ("no-link-signal-or-laser-fail", 5), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmAlarmConditionPort8.setStatus('mandatory')
if mibBuilder.loadTexts: mdmAlarmConditionPort8.setDescription("The alarm trigger mode at port 8: 'disable', i.e. no alarm is triggered, 'no-link-signal', i.e. an alarm is triggered if the link is down, 'laser-fail', i.e. an alarm is triggered if the laser diode is defective, or 'no-link-signal-or-laser-fail', i.e. the link is down or the laser diode is defective.")
fmePortTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2), )
if mibBuilder.loadTexts: fmePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: fmePortTable.setDescription('This table contains information about all I/F ports of the FME units within all stacks.')
fmePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1), ).setIndexNames((0, "PANDATEL-FME-MODEM-MIB", "portRack"), (0, "PANDATEL-FME-MODEM-MIB", "portModem"), (0, "PANDATEL-FME-MODEM-MIB", "portPosition"), (0, "PANDATEL-FME-MODEM-MIB", "portPort"))
if mibBuilder.loadTexts: fmePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fmePortEntry.setDescription('The index of the table.')
portRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRack.setStatus('mandatory')
if mibBuilder.loadTexts: portRack.setDescription('The index of the stack the port belongs to.')
portModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portModem.setStatus('mandatory')
if mibBuilder.loadTexts: portModem.setDescription('The index of the FME unit the port belongs to.')
portPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPosition.setStatus('mandatory')
if mibBuilder.loadTexts: portPosition.setDescription("This entry displays the location of the corresponding port: 'local' or 'remote'. The port which belongs to a managed stack is 'local', the counterpart is 'remote'.")
portPort = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPort.setStatus('mandatory')
if mibBuilder.loadTexts: portPort.setDescription('The index of the port.')
portInterfaceEmulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portInterfaceEmulationMode.setStatus('mandatory')
if mibBuilder.loadTexts: portInterfaceEmulationMode.setDescription("Interface mode of the port: 'dte', 'dce', 'te', or 'nt'.")
mdmModemProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("e1", 2), ("t1", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemProperty.setStatus('mandatory')
if mibBuilder.loadTexts: mdmModemProperty.setDescription("The speed class of the port: 'e1' or 't1'.")
portClockSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dual", 2), ("single", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portClockSystem.setStatus('mandatory')
if mibBuilder.loadTexts: portClockSystem.setDescription("The clock system at the interface port: 'single' or 'dual'. The available values depend on the interface type.")
portClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("remote", 3), ("external", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: portClockSource.setDescription("The clock source at the interface port: 'internal', 'remote', or 'external'.")
portDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("other", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portDataRate.setStatus('mandatory')
if mibBuilder.loadTexts: portDataRate.setDescription('The data rate at the interface port in bits per seconds. The data rate at the remote counterpart changes simultaneously.')
portLocalCarrierDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("fo-link-and-remote-handshake", 2), ("fo-link", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLocalCarrierDetect.setStatus('mandatory')
if mibBuilder.loadTexts: portLocalCarrierDetect.setDescription("The data carrier detect mode at the interface: if set to 'fo-link-and-remote-handshake' the DCD signal (resp. I for X.21, etc.) follows link status and remote RTS (resp. C for X.21, etc.), if set to 'fo-link' the DCD signal follows link status only. Not available for units with G.703 onboard.")
portTDPhaseLocking = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 67), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("positive-clock-slope", 2), ("negative-clock-slope", 3), ("unknown", 99)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTDPhaseLocking.setStatus('mandatory')
if mibBuilder.loadTexts: portTDPhaseLocking.setDescription("This entry defines the data phase locking for I/F data: 'positive-clock-slope' or 'negative-clock-slope'. For units with G.703 onboard the value 'positive-clock-slope' is valid only.")
portLineBuiltOut = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 601, 2, 1, 68), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 100))).clone(namedValues=NamedValues(("other", 1), ("itu-rec-g703", 2), ("dsx-1-0to133-ft", 3), ("dsx-1-133to266-ft", 4), ("dsx-1-266to399-ft", 5), ("dsx-1-399to533-ft", 6), ("dsx-1-533to655-ft", 7), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLineBuiltOut.setStatus('mandatory')
if mibBuilder.loadTexts: portLineBuiltOut.setDescription('The G.703 transmission mode of the unit. Valid for units with G.703 onboard only.')
mibBuilder.exportSymbols("PANDATEL-FME-MODEM-MIB", mdmAlarmConditionPort8=mdmAlarmConditionPort8, mdmRack=mdmRack, portPosition=portPosition, mdmAlarmConditionPort7=mdmAlarmConditionPort7, portRack=portRack, portInterfaceEmulationMode=portInterfaceEmulationMode, fme=fme, mdmActiveLink=mdmActiveLink, portLineBuiltOut=portLineBuiltOut, fmePortTable=fmePortTable, mdmPosition=mdmPosition, fmeTableEntry=fmeTableEntry, fmePortEntry=fmePortEntry, fmeModemTable=fmeModemTable, portPort=portPort, fme_modem=fme_modem, mdmModem=mdmModem, mdmModemName=mdmModemName, mdmModemProperty=mdmModemProperty, portModem=portModem, portClockSystem=portClockSystem, portTDPhaseLocking=portTDPhaseLocking, portLocalCarrierDetect=portLocalCarrierDetect, portClockSource=portClockSource, portDataRate=portDataRate)
