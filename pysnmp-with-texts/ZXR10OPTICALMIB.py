#
# PySNMP MIB module ZXR10OPTICALMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10OPTICALMIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Gauge32, Counter32, ObjectIdentity, IpAddress, Counter64, MibIdentifier, Integer32, Bits, iso, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter32", "ObjectIdentity", "IpAddress", "Counter64", "MibIdentifier", "Integer32", "Bits", "iso", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxr10interfaces, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10interfaces")
zxr10OpticalMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11))
if mibBuilder.loadTexts: zxr10OpticalMIB.setLastUpdated('200810070000Z')
if mibBuilder.loadTexts: zxr10OpticalMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: zxr10OpticalMIB.setContactInfo('ZTE Corporation Nanjing Institute of ZTE Corporation No.68 Zijinghua Rd. Yuhuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: zxr10OpticalMIB.setDescription('ZXROS v4.8.30 Optical info query and configuration MIB')
class DisplayString(OctetString):
    pass

class OpticalOnline(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("offline", 0), ("online", 1))

class SonetComplianceCodesType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("null", 0), ("short-reach", 1), ("intermediate-reach", 2), ("long-reach", 4), ("very-Long-reach", 8))

class SonetComplianceCodesSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))
    namedValues = NamedValues(("oc3", 1), ("oc12", 2), ("oc48", 4), ("oc192", 8))

class GigabitEthernetComplianceCodesType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("null", 0), ("base-sx-1000", 1), ("base-lx-1000", 2), ("base-lx-100", 3), ("base-cx-1000", 4), ("base-fx-100", 5), ("base_bx", 6), ("base_px", 7), ("base-t-1000", 8), ("base-t-100", 9))

class InfinibandComplianceCodesType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("null", 0), ("copper-Passiv", 1), ("copper-Active", 2), ("lx", 4), ("sx", 8))

class GigabitEthernetComplianceCodesSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("m-1000", 1), ("g-10", 2), ("g-40", 3), ("g-100", 4))

class InfinibandComplianceCodesSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("m-1000", 1), ("g-10", 2))

zxr10OpticalTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1), )
if mibBuilder.loadTexts: zxr10OpticalTable.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalTable.setDescription('Ethnet configuration table')
zxr10OpticalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1), ).setIndexNames((0, "ZXR10OPTICALMIB", "zxr10OpticalIfIndex"))
if mibBuilder.loadTexts: zxr10OpticalEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalEntry.setDescription('')
zxr10OpticalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalIfIndex.setDescription('Physical Ethnet interface ifIndex')
zxr10OpticalIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalIfName.setDescription('Physical Ethnet interface ifName')
zxr10OpticalOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 3), OpticalOnline()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalOnline.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalOnline.setDescription('Optical Module is Online')
zxr10OpticalFpType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalFpType.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalFpType.setDescription('Optical Module Info FpType')
zxr10OpticalSonetComplianceCodesType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 5), SonetComplianceCodesType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSonetComplianceCodesType.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSonetComplianceCodesType.setDescription('Sonet Compliance Codes Type')
zxr10OpticalSonetComplianceCodesSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 6), SonetComplianceCodesSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSonetComplianceCodesSpeed.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSonetComplianceCodesSpeed.setDescription('Sonet Compliance Codes Speed')
zxr10OpticalGigabitEthernetComplianceCodesType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalGigabitEthernetComplianceCodesType.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalGigabitEthernetComplianceCodesType.setDescription('Gigabit Ethernet Compliance Codes Type')
zxr10OpticalGigabitEthernetComplianceCodesSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 8), GigabitEthernetComplianceCodesSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalGigabitEthernetComplianceCodesSpeed.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalGigabitEthernetComplianceCodesSpeed.setDescription('Gigabit Ethernet Compliance Codes Speed')
zxr10OpticalInfinibandComplianceCodesType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 9), InfinibandComplianceCodesType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalInfinibandComplianceCodesType.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalInfinibandComplianceCodesType.setDescription('Infiniband Compliance Codes Type')
zxr10OpticalInfinibandComplianceCodesSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 10), InfinibandComplianceCodesSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalInfinibandComplianceCodesSpeed.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalInfinibandComplianceCodesSpeed.setDescription('Infiniband Compliance Codes Speed')
zxr10OpticalDisSMFkm = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalDisSMFkm.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalDisSMFkm.setDescription('Optical Module Info DisSMFkm')
zxr10OpticalDis9um = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalDis9um.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalDis9um.setDescription('Optical Module Info Dis9_125um')
zxr10OpticalDis50um = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalDis50um.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalDis50um.setDescription('Optical Module Info Dis50_125um')
zxr10OpticalDis62um = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalDis62um.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalDis62um.setDescription('Optical Module Info Dis62_125um')
zxr10OpticalDiscopperLine = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalDiscopperLine.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalDiscopperLine.setDescription('Optical Module Info DiscopperLine')
zxr10OpticalSWaveLenth = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSWaveLenth.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSWaveLenth.setDescription('Optical Module Info S_waveLenth')
zxr10OpticalSWaveLenthValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSWaveLenthValid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSWaveLenthValid.setDescription('Optical Module Info S_waveLenthValid')
zxr10OpticalSRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPower.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPower.setDescription('Optical Module Info S_rxPower')
zxr10OpticalSRxPowerValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerValid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerValid.setDescription('Optical Module Info S_rxPowerValid')
zxr10OpticalSTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPower.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPower.setDescription('Optical Module Info S_txPower')
zxr10OpticalSTxPowerValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerValid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerValid.setDescription('Optical Module Info S_txPowerValid')
zxr10OpticalSTxCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrent.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrent.setDescription('Optical Module Info S_txCurren')
zxr10OpticalSTxCurrentValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentValid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentValid.setDescription('Optical Module Info S_txCurrentValid')
zxr10OpticalSTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperature.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperature.setDescription('Optical Module Info S_temperature')
zxr10OpticalSTemperatureValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureValid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureValid.setDescription('Optical Module Info S_temperatureValid')
zxr10Optical33SVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10Optical33SVoltage.setStatus('current')
if mibBuilder.loadTexts: zxr10Optical33SVoltage.setDescription('Optical Module Info 3.3 S_voltage')
zxr10Optical33SVoltageValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10Optical33SVoltageValid.setStatus('current')
if mibBuilder.loadTexts: zxr10Optical33SVoltageValid.setDescription('Optical Module Info 3.3 S_voltageValid')
zxr10Optical5SVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10Optical5SVoltage.setStatus('current')
if mibBuilder.loadTexts: zxr10Optical5SVoltage.setDescription('Optical Module Info 5 S_voltage')
zxr10Optical5SVoltageValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10Optical5SVoltageValid.setStatus('current')
if mibBuilder.loadTexts: zxr10Optical5SVoltageValid.setDescription('Optical Module Info 5 S_voltageValid')
zxr10OpticalVName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalVName.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalVName.setDescription('Optical Module Info VName')
zxr10OpticalVPn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalVPn.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalVPn.setDescription('Optical Module Info VPn')
zxr10OpticalRev = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalRev.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalRev.setDescription('Optical Module Info Rev')
zxr10OpticalVSn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 33), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalVSn.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalVSn.setDescription('Optical Module Info VSn')
zxr10OpticalSRxPowerChannel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 34), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel1.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel1.setDescription('Optical Module Info Channel1 S_rxPower')
zxr10OpticalSRxPowerChannel1Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel1Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel1Valid.setDescription('Optical Module Info Channel1 S_rxPowerValid')
zxr10OpticalSRxPowerChannel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 36), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel2.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel2.setDescription('Optical Module Info Channel2 S_rxPower')
zxr10OpticalSRxPowerChannel2Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel2Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel2Valid.setDescription('Optical Module Info Channel2 S_rxPowerValid')
zxr10OpticalSRxPowerChannel3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 38), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel3.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel3.setDescription('Optical Module Info Channel3 S_rxPower')
zxr10OpticalSRxPowerChannel3Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel3Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel3Valid.setDescription('Optical Module Info Channel3 S_rxPowerValid')
zxr10OpticalSRxPowerChannel4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 40), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel4.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel4.setDescription('Optical Module Info Channel4 S_rxPower')
zxr10OpticalSRxPowerChannel4Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel4Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSRxPowerChannel4Valid.setDescription('Optical Module Info Channel4 S_rxPowerValid')
zxr10OpticalSTxPowerChannel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 42), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel1.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel1.setDescription('Optical Module Info Channel1 S_txPower')
zxr10OpticalSTxPowerChannel1Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel1Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel1Valid.setDescription('Optical Module Info Channel1 S_txPowerValid')
zxr10OpticalSTxPowerChannel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 44), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel2.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel2.setDescription('Optical Module Info Channel2 S_txPower')
zxr10OpticalSTxPowerChannel2Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel2Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel2Valid.setDescription('Optical Module Info Channel2 S_txPowerValid')
zxr10OpticalSTxPowerChannel3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 46), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel3.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel3.setDescription('Optical Module Info Channel3 S_txPower')
zxr10OpticalSTxPowerChannel3Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel3Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel3Valid.setDescription('Optical Module Info Channel3 S_txPowerValid')
zxr10OpticalSTxPowerChannel4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 48), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel4.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel4.setDescription('Optical Module Info Channel4 S_txPower')
zxr10OpticalSTxPowerChannel4Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel4Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxPowerChannel4Valid.setDescription('Optical Module Info Channel4 S_txPowerValid')
zxr10OpticalSTxCurrentChannel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 50), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel1.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel1.setDescription('Optical Module Info Channel1 S_txCurren')
zxr10OpticalSTxCurrentChannel1Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel1Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel1Valid.setDescription('Optical Module Info Channel1 S_txCurrentValid')
zxr10OpticalSTxCurrentChannel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 52), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel2.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel2.setDescription('Optical Module Info Channel2 S_txCurren')
zxr10OpticalSTxCurrentChannel2Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel2Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel2Valid.setDescription('Optical Module Info Channel2 S_txCurrentValid')
zxr10OpticalSTxCurrentChannel3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 54), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel3.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel3.setDescription('Optical Module Info Channel3 S_txCurren')
zxr10OpticalSTxCurrentChannel3Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel3Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel3Valid.setDescription('Optical Module Info Channel3 S_txCurrentValid')
zxr10OpticalSTxCurrentChannel4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 56), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel4.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel4.setDescription('Optical Module Info Channel4 S_txCurren')
zxr10OpticalSTxCurrentChannel4Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel4Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTxCurrentChannel4Valid.setDescription('Optical Module Info Channel4 S_txCurrentValid')
zxr10OpticalSTemperatureChannel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 58), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel1.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel1.setDescription('Optical Module Info Channel1 S_temperature')
zxr10OpticalSTemperatureChannel1Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 59), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel1Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel1Valid.setDescription('Optical Module Info Channel1 S_temperatureValid')
zxr10OpticalSTemperatureChannel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 60), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel2.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel2.setDescription('Optical Module Info Channel2 S_temperature')
zxr10OpticalSTemperatureChannel2Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 61), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel2Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel2Valid.setDescription('Optical Module Info Channel2 S_temperatureValid')
zxr10OpticalSTemperatureChannel3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 62), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel3.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel3.setDescription('Optical Module Info Channel3 S_temperature')
zxr10OpticalSTemperatureChannel3Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 63), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel3Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel3Valid.setDescription('Optical Module Info Channel3 S_temperatureValid')
zxr10OpticalSTemperatureChannel4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 64), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel4.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel4.setDescription('Optical Module Info Channel4 S_temperature')
zxr10OpticalSTemperatureChannel4Valid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 11, 1, 1, 65), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel4Valid.setStatus('current')
if mibBuilder.loadTexts: zxr10OpticalSTemperatureChannel4Valid.setDescription('Optical Module Info Channel4 S_temperatureValid')
mibBuilder.exportSymbols("ZXR10OPTICALMIB", zxr10OpticalEntry=zxr10OpticalEntry, zxr10OpticalGigabitEthernetComplianceCodesType=zxr10OpticalGigabitEthernetComplianceCodesType, zxr10OpticalSRxPowerChannel2Valid=zxr10OpticalSRxPowerChannel2Valid, zxr10OpticalDis50um=zxr10OpticalDis50um, zxr10Optical5SVoltage=zxr10Optical5SVoltage, zxr10OpticalDis62um=zxr10OpticalDis62um, zxr10OpticalOnline=zxr10OpticalOnline, zxr10OpticalSTxPowerChannel3=zxr10OpticalSTxPowerChannel3, zxr10OpticalVName=zxr10OpticalVName, zxr10OpticalSTxCurrentChannel4Valid=zxr10OpticalSTxCurrentChannel4Valid, zxr10OpticalDiscopperLine=zxr10OpticalDiscopperLine, zxr10OpticalRev=zxr10OpticalRev, zxr10OpticalSTemperatureChannel1=zxr10OpticalSTemperatureChannel1, zxr10OpticalSRxPowerValid=zxr10OpticalSRxPowerValid, zxr10OpticalSRxPowerChannel1=zxr10OpticalSRxPowerChannel1, zxr10OpticalSRxPower=zxr10OpticalSRxPower, zxr10OpticalFpType=zxr10OpticalFpType, SonetComplianceCodesSpeed=SonetComplianceCodesSpeed, InfinibandComplianceCodesSpeed=InfinibandComplianceCodesSpeed, zxr10OpticalSTxCurrentChannel4=zxr10OpticalSTxCurrentChannel4, GigabitEthernetComplianceCodesSpeed=GigabitEthernetComplianceCodesSpeed, zxr10OpticalSTemperatureChannel3=zxr10OpticalSTemperatureChannel3, zxr10OpticalSRxPowerChannel4=zxr10OpticalSRxPowerChannel4, zxr10OpticalSTxCurrentChannel1=zxr10OpticalSTxCurrentChannel1, zxr10OpticalSTxPowerChannel1=zxr10OpticalSTxPowerChannel1, zxr10OpticalSTemperature=zxr10OpticalSTemperature, zxr10OpticalSTemperatureChannel2=zxr10OpticalSTemperatureChannel2, zxr10OpticalInfinibandComplianceCodesType=zxr10OpticalInfinibandComplianceCodesType, InfinibandComplianceCodesType=InfinibandComplianceCodesType, zxr10OpticalSTxCurrentChannel2Valid=zxr10OpticalSTxCurrentChannel2Valid, zxr10OpticalDis9um=zxr10OpticalDis9um, PYSNMP_MODULE_ID=zxr10OpticalMIB, zxr10OpticalSTxPowerChannel2Valid=zxr10OpticalSTxPowerChannel2Valid, zxr10OpticalSRxPowerChannel2=zxr10OpticalSRxPowerChannel2, zxr10OpticalSonetComplianceCodesType=zxr10OpticalSonetComplianceCodesType, zxr10OpticalSonetComplianceCodesSpeed=zxr10OpticalSonetComplianceCodesSpeed, zxr10OpticalSTxCurrentValid=zxr10OpticalSTxCurrentValid, zxr10Optical33SVoltageValid=zxr10Optical33SVoltageValid, zxr10OpticalSTemperatureValid=zxr10OpticalSTemperatureValid, zxr10OpticalSTxPower=zxr10OpticalSTxPower, zxr10OpticalSTxCurrentChannel3Valid=zxr10OpticalSTxCurrentChannel3Valid, zxr10OpticalSTemperatureChannel2Valid=zxr10OpticalSTemperatureChannel2Valid, zxr10OpticalSTxCurrentChannel1Valid=zxr10OpticalSTxCurrentChannel1Valid, zxr10OpticalIfIndex=zxr10OpticalIfIndex, zxr10OpticalSTxCurrent=zxr10OpticalSTxCurrent, zxr10OpticalMIB=zxr10OpticalMIB, DisplayString=DisplayString, GigabitEthernetComplianceCodesType=GigabitEthernetComplianceCodesType, zxr10Optical5SVoltageValid=zxr10Optical5SVoltageValid, zxr10OpticalTable=zxr10OpticalTable, zxr10OpticalVPn=zxr10OpticalVPn, zxr10OpticalSWaveLenthValid=zxr10OpticalSWaveLenthValid, zxr10OpticalIfName=zxr10OpticalIfName, OpticalOnline=OpticalOnline, zxr10OpticalSTxPowerChannel4Valid=zxr10OpticalSTxPowerChannel4Valid, zxr10OpticalSTxPowerValid=zxr10OpticalSTxPowerValid, zxr10OpticalGigabitEthernetComplianceCodesSpeed=zxr10OpticalGigabitEthernetComplianceCodesSpeed, SonetComplianceCodesType=SonetComplianceCodesType, zxr10OpticalSTxCurrentChannel3=zxr10OpticalSTxCurrentChannel3, zxr10OpticalDisSMFkm=zxr10OpticalDisSMFkm, zxr10OpticalSWaveLenth=zxr10OpticalSWaveLenth, zxr10OpticalSTemperatureChannel1Valid=zxr10OpticalSTemperatureChannel1Valid, zxr10OpticalSTxPowerChannel4=zxr10OpticalSTxPowerChannel4, zxr10OpticalSTxCurrentChannel2=zxr10OpticalSTxCurrentChannel2, zxr10OpticalVSn=zxr10OpticalVSn, zxr10Optical33SVoltage=zxr10Optical33SVoltage, zxr10OpticalSTxPowerChannel1Valid=zxr10OpticalSTxPowerChannel1Valid, zxr10OpticalSRxPowerChannel3Valid=zxr10OpticalSRxPowerChannel3Valid, zxr10OpticalSTemperatureChannel4=zxr10OpticalSTemperatureChannel4, zxr10OpticalSRxPowerChannel3=zxr10OpticalSRxPowerChannel3, zxr10OpticalSTxPowerChannel3Valid=zxr10OpticalSTxPowerChannel3Valid, zxr10OpticalSTemperatureChannel3Valid=zxr10OpticalSTemperatureChannel3Valid, zxr10OpticalInfinibandComplianceCodesSpeed=zxr10OpticalInfinibandComplianceCodesSpeed, zxr10OpticalSTxPowerChannel2=zxr10OpticalSTxPowerChannel2, zxr10OpticalSRxPowerChannel4Valid=zxr10OpticalSRxPowerChannel4Valid, zxr10OpticalSRxPowerChannel1Valid=zxr10OpticalSRxPowerChannel1Valid, zxr10OpticalSTemperatureChannel4Valid=zxr10OpticalSTemperatureChannel4Valid)