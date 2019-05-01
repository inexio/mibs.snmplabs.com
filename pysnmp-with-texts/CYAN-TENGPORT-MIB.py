#
# PySNMP MIB module CYAN-TENGPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-TENGPORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanOffOnTc, CyanOpStateTc, CyanTPConnectionStateTc, CyanSecServiceStateTc, CyanAdminStateTc, CyanXGOSignalTypeTc, CyanOpStateQualTc, CyanEnDisabledTc, CyanTxControlTc, CyanLoopbackControlTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanOffOnTc", "CyanOpStateTc", "CyanTPConnectionStateTc", "CyanSecServiceStateTc", "CyanAdminStateTc", "CyanXGOSignalTypeTc", "CyanOpStateQualTc", "CyanEnDisabledTc", "CyanTxControlTc", "CyanLoopbackControlTc")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Bits, iso, ObjectIdentity, NotificationType, Counter64, TimeTicks, Counter32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "iso", "ObjectIdentity", "NotificationType", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyanTENGPortModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150))
cyanTENGPortModule.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanTENGPortModule.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanTENGPortModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanTENGPortModule.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanTENGPortModule.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanTENGPortModule.setDescription('MIB module for Ten Gig Port')
cyanTENGPortMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1))
cyanTENGPortTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1), )
if mibBuilder.loadTexts: cyanTENGPortTable.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortTable.setDescription('A list of TENGPort entries.')
cyanTENGPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1), ).setIndexNames((0, "CYAN-TENGPORT-MIB", "cyanTENGPortShelfId"), (0, "CYAN-TENGPORT-MIB", "cyanTENGPortModuleId"), (0, "CYAN-TENGPORT-MIB", "cyanTENGPortXcvrId"), (0, "CYAN-TENGPORT-MIB", "cyanTENGPortPortId"))
if mibBuilder.loadTexts: cyanTENGPortEntry.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortEntry.setDescription('An entry of TENGPort.')
cyanTENGPortShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanTENGPortShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortShelfId.setDescription('Shelf Id')
cyanTENGPortModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanTENGPortModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortModuleId.setDescription('Module Id')
cyanTENGPortXcvrId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanTENGPortXcvrId.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortXcvrId.setDescription('Transceiver Id')
cyanTENGPortPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 4), Unsigned32())
if mibBuilder.loadTexts: cyanTENGPortPortId.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortPortId.setDescription('Port Id')
cyanTENGPortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 5), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortAdminState.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortAdminState.setDescription('Administrative state')
cyanTENGPortAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortAutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortAutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanTENGPortConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 7), CyanTPConnectionStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortConnectionState.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortConnectionState.setDescription('Termination point connection state')
cyanTENGPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortDescription.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortDescription.setDescription('Description')
cyanTENGPortExternalFiberMultishelfLink = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 9), CyanEnDisabledTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortExternalFiberMultishelfLink.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortExternalFiberMultishelfLink.setDescription('Assign a port to an inter-node link')
cyanTENGPortExternalFiberRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 45))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortExternalFiberRemotePort.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortExternalFiberRemotePort.setDescription('Remote connection point of the inter-node link')
cyanTENGPortLoopbackControl = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 11), CyanLoopbackControlTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortLoopbackControl.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortLoopbackControl.setDescription('Port loopback control')
cyanTENGPortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 12), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortOperState.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortOperState.setDescription('Primary Operation State')
cyanTENGPortOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 13), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortOperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortOperStateQual.setDescription('Operation state qualifier')
cyanTENGPortRxPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortRxPwr.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortRxPwr.setDescription('RX Power')
cyanTENGPortSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 15), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortSecServState.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortSecServState.setDescription('Secondary service state')
cyanTENGPortSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 16), CyanXGOSignalTypeTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortSignalType.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortSignalType.setDescription('Client signal type or port mode')
cyanTENGPortTransmitControl = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 17), CyanTxControlTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortTransmitControl.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortTransmitControl.setDescription('Transmitter control')
cyanTENGPortTxPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortTxPwr.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortTxPwr.setDescription('TX Power')
cyanTENGPortTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 19), CyanOffOnTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanTENGPortTxStatus.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortTxStatus.setDescription('Transmitter status')
cyanTENGPortObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 20)).setObjects(("CYAN-TENGPORT-MIB", "cyanTENGPortAdminState"), ("CYAN-TENGPORT-MIB", "cyanTENGPortAutoinserviceSoakTimeSec"), ("CYAN-TENGPORT-MIB", "cyanTENGPortConnectionState"), ("CYAN-TENGPORT-MIB", "cyanTENGPortDescription"), ("CYAN-TENGPORT-MIB", "cyanTENGPortExternalFiberMultishelfLink"), ("CYAN-TENGPORT-MIB", "cyanTENGPortExternalFiberRemotePort"), ("CYAN-TENGPORT-MIB", "cyanTENGPortLoopbackControl"), ("CYAN-TENGPORT-MIB", "cyanTENGPortOperState"), ("CYAN-TENGPORT-MIB", "cyanTENGPortOperStateQual"), ("CYAN-TENGPORT-MIB", "cyanTENGPortRxPwr"), ("CYAN-TENGPORT-MIB", "cyanTENGPortSecServState"), ("CYAN-TENGPORT-MIB", "cyanTENGPortSignalType"), ("CYAN-TENGPORT-MIB", "cyanTENGPortTransmitControl"), ("CYAN-TENGPORT-MIB", "cyanTENGPortTxPwr"), ("CYAN-TENGPORT-MIB", "cyanTENGPortTxStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanTENGPortObjectGroup = cyanTENGPortObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortObjectGroup.setDescription('Group of objects that comes with TENGPort module')
cyanTENGPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 30)).setObjects(("CYAN-TENGPORT-MIB", "cyanTENGPortObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanTENGPortCompliance = cyanTENGPortCompliance.setStatus('current')
if mibBuilder.loadTexts: cyanTENGPortCompliance.setDescription('The basic info needed to be a cyan TENGPort')
mibBuilder.exportSymbols("CYAN-TENGPORT-MIB", PYSNMP_MODULE_ID=cyanTENGPortModule, cyanTENGPortCompliance=cyanTENGPortCompliance, cyanTENGPortAutoinserviceSoakTimeSec=cyanTENGPortAutoinserviceSoakTimeSec, cyanTENGPortExternalFiberMultishelfLink=cyanTENGPortExternalFiberMultishelfLink, cyanTENGPortLoopbackControl=cyanTENGPortLoopbackControl, cyanTENGPortOperStateQual=cyanTENGPortOperStateQual, cyanTENGPortTransmitControl=cyanTENGPortTransmitControl, cyanTENGPortOperState=cyanTENGPortOperState, cyanTENGPortAdminState=cyanTENGPortAdminState, cyanTENGPortTxStatus=cyanTENGPortTxStatus, cyanTENGPortModuleId=cyanTENGPortModuleId, cyanTENGPortConnectionState=cyanTENGPortConnectionState, cyanTENGPortShelfId=cyanTENGPortShelfId, cyanTENGPortExternalFiberRemotePort=cyanTENGPortExternalFiberRemotePort, cyanTENGPortMibObjects=cyanTENGPortMibObjects, cyanTENGPortEntry=cyanTENGPortEntry, cyanTENGPortXcvrId=cyanTENGPortXcvrId, cyanTENGPortPortId=cyanTENGPortPortId, cyanTENGPortSecServState=cyanTENGPortSecServState, cyanTENGPortTable=cyanTENGPortTable, cyanTENGPortSignalType=cyanTENGPortSignalType, cyanTENGPortDescription=cyanTENGPortDescription, cyanTENGPortTxPwr=cyanTENGPortTxPwr, cyanTENGPortObjectGroup=cyanTENGPortObjectGroup, cyanTENGPortModule=cyanTENGPortModule, cyanTENGPortRxPwr=cyanTENGPortRxPwr)
