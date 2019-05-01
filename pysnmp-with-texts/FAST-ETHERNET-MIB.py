#
# PySNMP MIB module FAST-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FAST-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ctFastEthernet, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFastEthernet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, iso, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, IpAddress, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "iso", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFastEthernetCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1))
ctMMACFENBCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2))
ctFastEthernetCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1), )
if mibBuilder.loadTexts: ctFastEthernetCtlTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCtlTable.setDescription('Provides a list of definitions and control objects over 100Base-X ports.')
ctFastEthernetCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1), ).setIndexNames((0, "FAST-ETHERNET-MIB", "ctFastEthernetCtlInterface"), (0, "FAST-ETHERNET-MIB", "ctFastEthernetCtlPortGroup"), (0, "FAST-ETHERNET-MIB", "ctFastEthernetCtlPort"))
if mibBuilder.loadTexts: ctFastEthernetCtlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCtlEntry.setDescription('Defines a particular entry containing objects pertaining to definition and control over 100Base-X ports.')
ctFastEthernetCtlInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFastEthernetCtlInterface.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCtlInterface.setDescription('The interface for which this fast ethernet information pertains.')
ctFastEthernetCtlPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFastEthernetCtlPortGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCtlPortGroup.setDescription('The port group for which this fast ethernet information pertains.')
ctFastEthernetCtlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFastEthernetCtlPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCtlPort.setDescription('The physical port for which this fast ethernet information pertains.')
ctFastEthernetLocalTechnologyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFastEthernetLocalTechnologyAbility.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetLocalTechnologyAbility.setDescription('This indicates the technology ability of the local hardware. The value of this object is the logical OR of all supported technologies. Where each technology is given the values below: other(1) Undefined, or ability not known Auto-Negotiation(2) Auto-Negotiation 10BASE-T(8) 10BASE-T 10BASE-TFD(16) Full duplex 10BASE-T 100BASE-TX(32) 100BASE-TX 100BASE-TXFD(64) Full Duplex 100BASE-TX 100BASE-T4(128) 100BASE-T4 100BASE-FX(256) 100BASE-FX 100BASE-FXFD(512) Full Duplex 100Base-FX For example a port which supported 100Base-TX(32), 100Base-TXFD(64), and Auto-Negotiation(2) would have a value of 98(32 + 64 + 2).')
ctFastEthernetCurrentOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFastEthernetCurrentOperationalMode.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCurrentOperationalMode.setDescription('Indicates the current operational mode of this port. The value of this object is the logical OR of current opertational mode and how we arrived at that mode, whether it be by Auto-Negotiation(2), Manual-Config(4) or default. Where each mode is given the values below: other(1) Initializing or no link, ability unknown Auto-Negotiation(2) Auto-Negotiation/Parallel Detection Manual-Config(4) Manually Configured 10BASE-T(8) 10BASE-T 10BASE-TFD(16) Full duplex 10BASE-T 100BASE-TX(32) 100BASE-TX 100BASE-TXFD(64) Full Duplex 100BASE-TX 100BASE-T4(128) 100BASE-T4 100Base-FX(256) 100Base-FX 100Base-FXFD(512) Full Duplex 100Base-FX For example, a port operating at 100Base-TX(32) achieved through Auto-Negotiation(2) would have a value of 34(32 + 2). If the port was manually configured(4) for 100Base-TX(32) this object would have a value of 36(32 + 4). Values written to this object are limited to values read from ctFastEthernetLocalTechnologyAbility, with the addition of Manual-Config(4) but excluding other(1). Therefore if ctFastEthernetLocalTechnologyAbility has a value of 98 writing a value of 256 would result in an error. That is to say 100Base-FX is not supported on this port. A set to a value of Auto-Negotiation(2) will result in auto-negotiation being enabled and will cause link re-negotiation. Note: this re-negotiation will in every case cause temporary link loss during the link re-negotiation. Any other set with Auto-Negotiation(2) included will result in an error since you can not force an operational mode and auto-negotiation at the same time. A set to a value of Manual-Config(4) will result in auto-negotiation being disabled but the port staying at its current operational mode until device reset/power down at which time the port will come up in default mode. A subsequent read will indicate only the current operational mode achieved by default means. A set to any other value (port is being manually configured) must reflect a single ability. For example writing a value of 68 would result in auto-negotiation being disabled and the port being manually configured(4) for 100Base-TXFD(64). However a write of 100 would result in an error.')
ctFastEthernetAdvertisedTechnologyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFastEthernetAdvertisedTechnologyAbility.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetAdvertisedTechnologyAbility.setDescription('Indicates the advertised ability of the local hardware, but only becomes active on ports that have auto-negotiation enabled. For example a port which will advertise 100Base-TX(32) and 100Base-TXFD(64) ablilities would have a value of 96(32 + 64). A port that does not support auto-negotiation will be read as other(1). Values written to this object are limited to values read from ctFastEthernetLocalTechnologyAbility, excluding other(1) and Auto-Negotiation(2). Therefore if ctFastEthernetLocalTechnologyAbility has a value of 98 writing a value of 128 would result in an error. That is to say 100Base-T4 is not supported on this port. Furthermore, if ctFastEthernetLocalTechnologyAbility has a value that does not include Auto-Negotiation(2), writing any value will result in an error. That is to say that this port does not support Auto-Negotiation and therefore does not support ctFastEthernetAdvertisedTechnologyAbility. A successful set operation will result in immediate link re-negotiation if ctFastEthernetCurrentOperationalMode has a value that includes Auto-Negotiation(2)(meaning Auto-negotiation is enabled). Note: this re-negotiation will in every case cause temporary link loss during the link re-negotiation. If set to a value that is incompatible with ctFastEthernetReceivedTechnologyAbility, link negotiation will not be successful and will cause permanent link loss.')
ctFastEthernetReceivedTechnologyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFastEthernetReceivedTechnologyAbility.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetReceivedTechnologyAbility.setDescription('Indicates the advertised ability of the remote hardware, or link partner. The value of this object is the logical OR of all supported technologies. Where each technology is given the values below: other(1) Undefined Auto-Negotiation(2) Auto-Negotiation/Parallel Detection Not-Detected(4) Link Partner does not support Auto-Negotiation 10BASE-T(8) 10BASE-T 10BASE-TFD(16) Full duplex 10BASE-T 100BASE-TX(32) 100BASE-TX as defined in clause 25 100BASE-TXFD(64) Full Duplex 100BASE-TX 100BASE-T4(128) 100BASE-T4 as defined in clause 23 100Base-FX(256) 100Base-FX 100Base-FXFD(512) Full Duplex 100Base-FX For example a port which supports 100Base-TX(32), 100Base-TXFD(64), would have a value of 98(32 + 64 + Auto-Negotiation(2)). A read should always include Auto-Negotiation(2), unless the link partner does not support auto-negotiation, at which time the value will be Not-Detected(4) or auto-negotiation is disabled(or not supported) for this port at which time the value will be other(1).')
ctFastEthernetCtlTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFastEthernetCtlTableNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctFastEthernetCtlTableNumEntries.setDescription('The number of entries in the ctFastEthernetCtl Table.')
ctMMACFENBCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1), )
if mibBuilder.loadTexts: ctMMACFENBCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBCfgTable.setDescription('A table defining the capabilities of each port in regards to the MMAC Fast Ethernet Network Bus.')
ctMMACFENBCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1), ).setIndexNames((0, "FAST-ETHERNET-MIB", "ctMMACFENBCfgInterface"), (0, "FAST-ETHERNET-MIB", "ctMMACFENBCfgPortGroup"), (0, "FAST-ETHERNET-MIB", "ctMMACFENBCfgPort"))
if mibBuilder.loadTexts: ctMMACFENBCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBCfgEntry.setDescription('defines a particular entry containing port configuration information.')
ctMMACFENBCfgInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctMMACFENBCfgInterface.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBCfgInterface.setDescription('The interface for which this MMAC FENB information pertains.')
ctMMACFENBCfgPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctMMACFENBCfgPortGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBCfgPortGroup.setDescription('The port group for which this MMAC FENB information pertains.')
ctMMACFENBCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctMMACFENBCfgPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBCfgPort.setDescription('The physical port for which this MMAC FENB information pertains.')
ctMMACFENBOperCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctMMACFENBOperCapabilities.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBOperCapabilities.setDescription('This value indicates the current capabilities of this port. (1) Other (2) MMAC A Channel (4) MMAC FENB 1 (FENB= Fast Ethernet Network Bus) (8) MMAC FENB 2 (16) MMAC FENB 3 (32) Front Panel The value of this object is the logical OR of all supported capabilities.')
ctMMACFENBAdminCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctMMACFENBAdminCapabilities.setStatus('mandatory')
if mibBuilder.loadTexts: ctMMACFENBAdminCapabilities.setDescription('This value indicates the desired operational capabilities of this port. (1) Other (2) MMAC A Channel (4) MMAC FENB 1 (FENB= Fast Ethernet Network Bus) (8) MMAC FENB 2 (16) MMAC FENB 3 (32) Front Panel')
mibBuilder.exportSymbols("FAST-ETHERNET-MIB", ctMMACFENBCfg=ctMMACFENBCfg, ctFastEthernetCtlEntry=ctFastEthernetCtlEntry, ctFastEthernetCtlPort=ctFastEthernetCtlPort, ctFastEthernetCtlPortGroup=ctFastEthernetCtlPortGroup, ctMMACFENBCfgPortGroup=ctMMACFENBCfgPortGroup, ctMMACFENBOperCapabilities=ctMMACFENBOperCapabilities, ctMMACFENBCfgPort=ctMMACFENBCfgPort, ctMMACFENBCfgEntry=ctMMACFENBCfgEntry, ctFastEthernetCtlTableNumEntries=ctFastEthernetCtlTableNumEntries, ctMMACFENBCfgInterface=ctMMACFENBCfgInterface, ctFastEthernetReceivedTechnologyAbility=ctFastEthernetReceivedTechnologyAbility, ctFastEthernetCtlTable=ctFastEthernetCtlTable, ctFastEthernetCurrentOperationalMode=ctFastEthernetCurrentOperationalMode, ctFastEthernetAdvertisedTechnologyAbility=ctFastEthernetAdvertisedTechnologyAbility, ctFastEthernetCtlInterface=ctFastEthernetCtlInterface, ctMMACFENBAdminCapabilities=ctMMACFENBAdminCapabilities, ctFastEthernetCtl=ctFastEthernetCtl, ctFastEthernetLocalTechnologyAbility=ctFastEthernetLocalTechnologyAbility, ctMMACFENBCfgTable=ctMMACFENBCfgTable)
