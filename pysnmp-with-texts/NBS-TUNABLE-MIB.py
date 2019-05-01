#
# PySNMP MIB module NBS-TUNABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-TUNABLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, nbs = mibBuilder.importSymbols("NBS-CMMC-MIB", "InterfaceIndex", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, iso, IpAddress, Counter32, NotificationType, Bits, ModuleIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "iso", "IpAddress", "Counter32", "NotificationType", "Bits", "ModuleIdentity", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsTunableMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 203))
if mibBuilder.loadTexts: nbsTunableMib.setLastUpdated('200903300119Z')
if mibBuilder.loadTexts: nbsTunableMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsTunableMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsTunableMib.setDescription('MIB for representing Tunable Optics parameters')
nbsTunableGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 203, 1))
if mibBuilder.loadTexts: nbsTunableGrp.setStatus('current')
if mibBuilder.loadTexts: nbsTunableGrp.setDescription('MIB for representing Tunable Optics parameters')
nbsTunableChannelTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 203, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelTableSize.setDescription('The number of entries in nbsTunableChannelTable.')
nbsTunableChannelTable = MibTable((1, 3, 6, 1, 4, 1, 629, 203, 1, 2), )
if mibBuilder.loadTexts: nbsTunableChannelTable.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelTable.setDescription('A table to report and configure tunable optics settings.')
nbsTunableChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1), ).setIndexNames((0, "NBS-TUNABLE-MIB", "nbsTunableChannelIfIndex"))
if mibBuilder.loadTexts: nbsTunableChannelEntry.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelEntry.setDescription("Describes a setting for an interface's tunable optics.")
nbsTunableChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelIfIndex.setDescription("The Mib2 ifIndex of this optic's port")
nbsTunableChannelFreqStart = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 2), Integer32().clone(190100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqStart.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqStart.setDescription("The first allowable frequency for this tunable optic, in GigaHertz (GHz), unless FreqExponent != 9. For L-Band, ITU Grid 48 is '184800' For Q-Band, ITU Grid 48 is '184850' For C-Band, ITU Grid 1 is '190100' For H-Band, ITU Grid 1 is '190150' If GHz does not provide the appropriate resolution, the tunable optic may report a FreqExponent less than 9. If 32 bits is insufficient to cover the range in GHz, the tunable optic may report a FreqExponent greater than 9.")
nbsTunableChannelFreqEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 3), Integer32().clone(197200)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqEnd.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqEnd.setDescription("The last allowable frequency (inclusive) for this tunable optic, in GigaHertz (GHz), unless FreqExponent != 9. For L-Band, ITU Grid 99 is '189900' For Q-Band, ITU Grid 99 is '189950' For C-Band, ITU Grid 72 is '197200' For H-Band, ITU Grid 72 is '197250' If GHz does not provide the appropriate resolution, the tunable optic may report a FreqExponent less than 9. If 32 bits is insufficient to cover the range in GHz, the tunable optic may report a FreqExponent greater than 9.")
nbsTunableChannelFreqStep = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 4), Integer32().clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqStep.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqStep.setDescription('The spacing of the allowable frequencies that this tunable optic supports, in GigaHertz (GHz), unless FreqExponent != 9. 100 indicates the standard ITU grid spacing of 100GHz. For example, if this tunable optic supports both C and H band, or both Q and L band, FreqStep should report 50. If this tunable optic supports steps finer than 1GHz, the tunable optic may report a FreqExponent less than 9.')
nbsTunableChannelFreqExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 5), Integer32().clone(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqExponent.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqExponent.setDescription('The exponent of all the Freq values (including FreqStep). 9 (the default) indicates all units are in GigaHertz (GHz).')
nbsTunableChannelFreqAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsTunableChannelFreqAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqAdmin.setDescription('The administratively desired frequency of this tunable optic, in GigaHertz (GHz), unless FreqExponent != 9.')
nbsTunableChannelFreqOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqOper.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqOper.setDescription('The current operational frequency of this tunable optic, in GigaHertz (GHz), unless FreqExponent != 9.')
nbsTunableChannelFreqDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqDefault.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqDefault.setDescription('The default frequency of this tunable optic, in GigaHertz (GHz), unless FreqExponent != 9.')
mibBuilder.exportSymbols("NBS-TUNABLE-MIB", nbsTunableGrp=nbsTunableGrp, PYSNMP_MODULE_ID=nbsTunableMib, nbsTunableChannelTableSize=nbsTunableChannelTableSize, nbsTunableChannelFreqStep=nbsTunableChannelFreqStep, nbsTunableChannelEntry=nbsTunableChannelEntry, nbsTunableChannelFreqEnd=nbsTunableChannelFreqEnd, nbsTunableChannelFreqExponent=nbsTunableChannelFreqExponent, nbsTunableChannelFreqOper=nbsTunableChannelFreqOper, nbsTunableChannelTable=nbsTunableChannelTable, nbsTunableChannelFreqAdmin=nbsTunableChannelFreqAdmin, nbsTunableMib=nbsTunableMib, nbsTunableChannelFreqStart=nbsTunableChannelFreqStart, nbsTunableChannelIfIndex=nbsTunableChannelIfIndex, nbsTunableChannelFreqDefault=nbsTunableChannelFreqDefault)
