import 'package:flutter/material.dart';

import '../config.dart';
import 'card_timer.dart';
import 'card_title.dart';

/// A card in the Lento deck.
class LentoCard extends StatelessWidget {
  final String cardId;

  const LentoCard({super.key, required this.cardId});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 350.0,
        height: 450.0,
        child: Container(
            decoration: const BoxDecoration(
                borderRadius: Config.defaultBorderRadius,
                boxShadow: [Config.defaultShadow]),
            child: Card(
                child: Padding(
                    padding: const EdgeInsets.all(Config.defaultElementSpacing),
                    child: SingleChildScrollView(
                        child: Center(
                            child: Wrap(
                                direction: Axis.vertical,
                                spacing: Config.defaultElementSpacing,
                                children: [
                          CardTitle(
                            cardId: cardId,
                          ),
                          CardTimer(
                            cardId: cardId,
                            startingColour:
                                Theme.of(context).colorScheme.surface,
                          )
                        ])))))));
  }
}