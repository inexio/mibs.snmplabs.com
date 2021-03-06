#
# PySNMP MIB module NOKIAVPN-IPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIAVPN-IPSEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
nokiaVPNModules, ipsec = mibBuilder.importSymbols("NOKIAVPN-MIB", "nokiaVPNModules", "ipsec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, Unsigned32, Counter32, NotificationType, iso, IpAddress, TimeTicks, ModuleIdentity, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter32", "NotificationType", "iso", "IpAddress", "TimeTicks", "ModuleIdentity", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nokiaVPNIPSECMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 5, 3))
nokiaVPNIPSECMIB.setRevisions(('2001-01-18 00:00',))
if mibBuilder.loadTexts: nokiaVPNIPSECMIB.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: nokiaVPNIPSECMIB.setOrganization('Nokia Internet Communications')
replayStats = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1))
naIKEStats = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2))
naAHStats = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3))
naESPStats = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4))
naKeyStats = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5))
replayStatsWraps = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatsWraps.setStatus('current')
replayStatsReplays = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatsReplays.setStatus('current')
replayStatsoutofrange = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatsoutofrange.setStatus('current')
replayStatstimewarps = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatstimewarps.setStatus('current')
replayStatsstale = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatsstale.setStatus('current')
replayStatsreset = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatsreset.setStatus('current')
replayStatsdeferred = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replayStatsdeferred.setStatus('current')
naIKEStatsbadhash = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsbadhash.setStatus('current')
naIKEStatsbadsig = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsbadsig.setStatus('current')
naIKEStatsinvalidcookies = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsinvalidcookies.setStatus('current')
naIKEStatsacounts = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsacounts.setStatus('current')
naIKEStatsmainmodes = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsmainmodes.setStatus('current')
naIKEStatsquickmodes = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsquickmodes.setStatus('current')
naIKEStatsaggressivemodes = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsaggressivemodes.setStatus('current')
naIKEStatsnewgroupmodes = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsnewgroupmodes.setStatus('current')
naIKEStatsfailedsend = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsfailedsend.setStatus('current')
naIKEStatstotalnetwork = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstotalnetwork.setStatus('current')
naIKEStatstotalsend = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstotalsend.setStatus('current')
naIKEStatstotalsaapi = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstotalsaapi.setStatus('current')
naIKEStatstotalipc = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstotalipc.setStatus('current')
naIKEStatstotalmanual = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstotalmanual.setStatus('current')
naIKEStatstotalauto = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstotalauto.setStatus('current')
naIKEStatstransitions = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatstransitions.setStatus('current')
naIKEStatssentsa = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentsa.setStatus('current')
naIKEStatssentipsecsapair = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentipsecsapair.setStatus('current')
naIKEStatssentpacket = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentpacket.setStatus('current')
naIKEStatsrecvsa = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvsa.setStatus('current')
naIKEStatsrecvipsecsapair = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvipsecsapair.setStatus('current')
naIKEStatsrecvpacket = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvpacket.setStatus('current')
naIKEStatssentinitialstate = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentinitialstate.setStatus('current')
naIKEStatssentflush = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentflush.setStatus('current')
naIKEStatssentcryptostate = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentcryptostate.setStatus('current')
naIKEStatssentacquire = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentacquire.setStatus('current')
naIKEStatssentipseclifetime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentipseclifetime.setStatus('current')
naIKEStatssentikelifetime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentikelifetime.setStatus('current')
naIKEStatssentdelete = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentdelete.setStatus('current')
naIKEStatssentselector = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentselector.setStatus('current')
naIKEStatsrecvjoin = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvjoin.setStatus('current')
naIKEStatsrecvrejoin = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvrejoin.setStatus('current')
naIKEStatsrecvflush = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvflush.setStatus('current')
naIKEStatsrecvcryptostate = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvcryptostate.setStatus('current')
naIKEStatsrecvacquire = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvacquire.setStatus('current')
naIKEStatsrecvipseclifetime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvipseclifetime.setStatus('current')
naIKEStatsrecvikelifetime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvikelifetime.setStatus('current')
naIKEStatsrecvdelete = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvdelete.setStatus('current')
naIKEStatsrecvselector = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvselector.setStatus('current')
naIKEStatssentinhibit = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatssentinhibit.setStatus('current')
naIKEStatsrecvinhibit = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 2, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naIKEStatsrecvinhibit.setStatus('current')
naAHStatssent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatssent.setStatus('current')
naAHStatstunnelsent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatstunnelsent.setStatus('current')
naAHStatstransportsent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatstransportsent.setStatus('current')
naAHStatsqueuesent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsqueuesent.setStatus('current')
naAHStatscpusent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatscpusent.setStatus('current')
naAHStatsidlesent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsidlesent.setStatus('current')
naAHStatshifnsent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatshifnsent.setStatus('current')
naAHStatsouterrors = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsouterrors.setStatus('current')
naAHStatsoutdrops = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsoutdrops.setStatus('current')
naAHStatsreceived = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsreceived.setStatus('current')
naAHStatstunnelrcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatstunnelrcvd.setStatus('current')
naAHStatstransportrcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatstransportrcvd.setStatus('current')
naAHStatsqueuercvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsqueuercvd.setStatus('current')
naAHStatscpurcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatscpurcvd.setStatus('current')
naAHStatsidlercvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsidlercvd.setStatus('current')
naAHStatshifnrcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatshifnrcvd.setStatus('current')
naAHStatsinerrors = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsinerrors.setStatus('current')
naAHStatsindrops = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsindrops.setStatus('current')
naAHStatssafailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatssafailures.setStatus('current')
naAHStatsreplay = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsreplay.setStatus('current')
naAHStatsfragments = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatsfragments.setStatus('current')
naAHStatshifnrefused = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatshifnrefused.setStatus('current')
naAHStatscpurefused = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 3, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naAHStatscpurefused.setStatus('current')
naESPStatssent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatssent.setStatus('current')
naESPStatstunnelsent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatstunnelsent.setStatus('current')
naESPStatstransportsent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatstransportsent.setStatus('current')
naESPStatsqueuesent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsqueuesent.setStatus('current')
naESPStatscpusent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatscpusent.setStatus('current')
naESPStatsidlesent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsidlesent.setStatus('current')
naESPStatshifnsent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatshifnsent.setStatus('current')
naESPStatsouterrors = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsouterrors.setStatus('current')
naESPStatsoutdrops = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsoutdrops.setStatus('current')
naESPStatsreceived = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsreceived.setStatus('current')
naESPStatstunnelrcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatstunnelrcvd.setStatus('current')
naESPStatstransportrcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatstransportrcvd.setStatus('current')
naESPStatsqueuercvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsqueuercvd.setStatus('current')
naESPStatscpurcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatscpurcvd.setStatus('current')
naESPStatsidlercvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsidlercvd.setStatus('current')
naESPStatshifnrcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatshifnrcvd.setStatus('current')
naESPStatsinerrors = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsinerrors.setStatus('current')
naESPStatsindrops = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsindrops.setStatus('current')
naESPStatssafailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatssafailures.setStatus('current')
naESPStatsreplay = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsreplay.setStatus('current')
naESPStatsfragments = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsfragments.setStatus('current')
naESPStatspadverifyfailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatspadverifyfailures.setStatus('current')
naESPStatssignaturefailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatssignaturefailures.setStatus('current')
naESPStatsweakkey = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatsweakkey.setStatus('current')
naESPStatskeyparity = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatskeyparity.setStatus('current')
naESPStatshifnrefused = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatshifnrefused.setStatus('current')
naESPStatscpurefused = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPStatscpurefused.setStatus('current')
naESPNatEncapsulate = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPNatEncapsulate.setStatus('current')
naESPNatDecapsulate = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 4, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naESPNatDecapsulate.setStatus('current')
naKeyStatssyntax = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatssyntax.setStatus('current')
naKeyStatsoutbound = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsoutbound.setStatus('current')
naKeyStatsinbound = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinbound.setStatus('current')
naKeyStatspending = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatspending.setStatus('current')
naKeyStatsselectors = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsselectors.setStatus('current')
naKeyStatsoutlast = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsoutlast.setStatus('current')
naKeyStatsouthash = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsouthash.setStatus('current')
naKeyStatsoutnew = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsoutnew.setStatus('current')
naKeyStatsinlast = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinlast.setStatus('current')
naKeyStatsinhash = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinhash.setStatus('current')
naKeyStatsrefresh = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsrefresh.setStatus('current')
naKeyStatsreaped = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsreaped.setStatus('current')
naKeyStatsreapedlarval = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsreapedlarval.setStatus('current')
naKeyStatsbypass = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsbypass.setStatus('current')
naKeyStatsdrop = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsdrop.setStatus('current')
naKeyStatsprotect = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsprotect.setStatus('current')
naKeyStatsinbypass = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinbypass.setStatus('current')
naKeyStatsindrop = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsindrop.setStatus('current')
naKeyStatsinprotect = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinprotect.setStatus('current')
naKeyStatsstallq = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsstallq.setStatus('current')
naKeyStatsnomatch = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsnomatch.setStatus('current')
naKeyStatsinnomatch = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinnomatch.setStatus('current')
naKeyStatsinmismatch = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsinmismatch.setStatus('current')
naKeyStatsadvmtusent = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsadvmtusent.setStatus('current')
naKeyStatsadvmturcvd = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsadvmturcvd.setStatus('current')
naKeyStatsphantom = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsphantom.setStatus('current')
naKeyStatsdynamicselectors = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatsdynamicselectors.setStatus('current')
naKeyStatstoolarge = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1, 5, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naKeyStatstoolarge.setStatus('current')
mibBuilder.exportSymbols("NOKIAVPN-IPSEC-MIB", naESPStatscpurcvd=naESPStatscpurcvd, naIKEStatsrecvpacket=naIKEStatsrecvpacket, naESPStatssent=naESPStatssent, naAHStatstransportsent=naAHStatstransportsent, naKeyStatsouthash=naKeyStatsouthash, naESPStatsouterrors=naESPStatsouterrors, naAHStatstunnelsent=naAHStatstunnelsent, naKeyStatsrefresh=naKeyStatsrefresh, naESPNatEncapsulate=naESPNatEncapsulate, naESPStatstransportrcvd=naESPStatstransportrcvd, naKeyStatsinmismatch=naKeyStatsinmismatch, naIKEStats=naIKEStats, naKeyStatsoutbound=naKeyStatsoutbound, naIKEStatsrecvikelifetime=naIKEStatsrecvikelifetime, naKeyStatsinnomatch=naKeyStatsinnomatch, naAHStatsfragments=naAHStatsfragments, naESPStatstransportsent=naESPStatstransportsent, naIKEStatsrecvacquire=naIKEStatsrecvacquire, naESPStatsindrops=naESPStatsindrops, naKeyStatssyntax=naKeyStatssyntax, naESPStatshifnsent=naESPStatshifnsent, naIKEStatssentcryptostate=naIKEStatssentcryptostate, naAHStatshifnrcvd=naAHStatshifnrcvd, naESPStatsfragments=naESPStatsfragments, naKeyStatsselectors=naKeyStatsselectors, naESPStatssignaturefailures=naESPStatssignaturefailures, naIKEStatssentinitialstate=naIKEStatssentinitialstate, naIKEStatstransitions=naIKEStatstransitions, naIKEStatsrecvipsecsapair=naIKEStatsrecvipsecsapair, naAHStatsqueuesent=naAHStatsqueuesent, naKeyStatsbypass=naKeyStatsbypass, naKeyStatsnomatch=naKeyStatsnomatch, naIKEStatssentipseclifetime=naIKEStatssentipseclifetime, naAHStatscpurcvd=naAHStatscpurcvd, naESPStatssafailures=naESPStatssafailures, naIKEStatsaggressivemodes=naIKEStatsaggressivemodes, naAHStatsidlercvd=naAHStatsidlercvd, naKeyStatsindrop=naKeyStatsindrop, naIKEStatsmainmodes=naIKEStatsmainmodes, naAHStatssent=naAHStatssent, naIKEStatsrecvrejoin=naIKEStatsrecvrejoin, naESPStatsidlercvd=naESPStatsidlercvd, naKeyStats=naKeyStats, replayStatsdeferred=replayStatsdeferred, naIKEStatsbadhash=naIKEStatsbadhash, naIKEStatstotalauto=naIKEStatstotalauto, naKeyStatsreaped=naKeyStatsreaped, naIKEStatssentipsecsapair=naIKEStatssentipsecsapair, naAHStatsoutdrops=naAHStatsoutdrops, naAHStatshifnrefused=naAHStatshifnrefused, naESPStatsinerrors=naESPStatsinerrors, naESPStatstunnelrcvd=naESPStatstunnelrcvd, naESPStatshifnrcvd=naESPStatshifnrcvd, naIKEStatsquickmodes=naIKEStatsquickmodes, naIKEStatssentselector=naIKEStatssentselector, naIKEStatssentdelete=naIKEStatssentdelete, naESPStatsoutdrops=naESPStatsoutdrops, naAHStatsindrops=naAHStatsindrops, naIKEStatsrecvinhibit=naIKEStatsrecvinhibit, naKeyStatsstallq=naKeyStatsstallq, naESPStatsqueuesent=naESPStatsqueuesent, naKeyStatsdynamicselectors=naKeyStatsdynamicselectors, naIKEStatsrecvflush=naIKEStatsrecvflush, naIKEStatsbadsig=naIKEStatsbadsig, naESPStatsreceived=naESPStatsreceived, naAHStatshifnsent=naAHStatshifnsent, replayStatsoutofrange=replayStatsoutofrange, PYSNMP_MODULE_ID=nokiaVPNIPSECMIB, naIKEStatssentinhibit=naIKEStatssentinhibit, naAHStatsreceived=naAHStatsreceived, replayStats=replayStats, naAHStatsouterrors=naAHStatsouterrors, replayStatsstale=replayStatsstale, naKeyStatsinhash=naKeyStatsinhash, naAHStatstransportrcvd=naAHStatstransportrcvd, naIKEStatssentflush=naIKEStatssentflush, naAHStatsidlesent=naAHStatsidlesent, naKeyStatsinbypass=naKeyStatsinbypass, naIKEStatssentpacket=naIKEStatssentpacket, naAHStatsreplay=naAHStatsreplay, naESPStatscpusent=naESPStatscpusent, naIKEStatstotalsaapi=naIKEStatstotalsaapi, naKeyStatsinprotect=naKeyStatsinprotect, naIKEStatsnewgroupmodes=naIKEStatsnewgroupmodes, replayStatsreset=replayStatsreset, naKeyStatsinbound=naKeyStatsinbound, naIKEStatsrecvcryptostate=naIKEStatsrecvcryptostate, nokiaVPNIPSECMIB=nokiaVPNIPSECMIB, naKeyStatsadvmtusent=naKeyStatsadvmtusent, naAHStatscpurefused=naAHStatscpurefused, naESPStatspadverifyfailures=naESPStatspadverifyfailures, naKeyStatsoutnew=naKeyStatsoutnew, naIKEStatstotalipc=naIKEStatstotalipc, naAHStatscpusent=naAHStatscpusent, naESPStatskeyparity=naESPStatskeyparity, naKeyStatsprotect=naKeyStatsprotect, naESPNatDecapsulate=naESPNatDecapsulate, naESPStats=naESPStats, naIKEStatsrecvselector=naIKEStatsrecvselector, naIKEStatstotalnetwork=naIKEStatstotalnetwork, naIKEStatssentsa=naIKEStatssentsa, naESPStatsreplay=naESPStatsreplay, naKeyStatspending=naKeyStatspending, naIKEStatsrecvsa=naIKEStatsrecvsa, naESPStatscpurefused=naESPStatscpurefused, replayStatsReplays=replayStatsReplays, naKeyStatstoolarge=naKeyStatstoolarge, naKeyStatsphantom=naKeyStatsphantom, naAHStatstunnelrcvd=naAHStatstunnelrcvd, naIKEStatstotalmanual=naIKEStatstotalmanual, naAHStatsqueuercvd=naAHStatsqueuercvd, replayStatsWraps=replayStatsWraps, naIKEStatstotalsend=naIKEStatstotalsend, naIKEStatsrecvipseclifetime=naIKEStatsrecvipseclifetime, naKeyStatsdrop=naKeyStatsdrop, naESPStatsweakkey=naESPStatsweakkey, naKeyStatsinlast=naKeyStatsinlast, naKeyStatsoutlast=naKeyStatsoutlast, naIKEStatssentacquire=naIKEStatssentacquire, naKeyStatsreapedlarval=naKeyStatsreapedlarval, naIKEStatsfailedsend=naIKEStatsfailedsend, naESPStatsidlesent=naESPStatsidlesent, naAHStats=naAHStats, naESPStatshifnrefused=naESPStatshifnrefused, naIKEStatsrecvjoin=naIKEStatsrecvjoin, replayStatstimewarps=replayStatstimewarps, naKeyStatsadvmturcvd=naKeyStatsadvmturcvd, naIKEStatsrecvdelete=naIKEStatsrecvdelete, naIKEStatssentikelifetime=naIKEStatssentikelifetime, naAHStatsinerrors=naAHStatsinerrors, naIKEStatsacounts=naIKEStatsacounts, naESPStatsqueuercvd=naESPStatsqueuercvd, naAHStatssafailures=naAHStatssafailures, naIKEStatsinvalidcookies=naIKEStatsinvalidcookies, naESPStatstunnelsent=naESPStatstunnelsent)
