
#pragma once
#include <AzCore/Component/Component.h>
#include <InteractiveTutorials/InteractiveTutorialsBus.h>

#include <AzToolsFramework/Entity/EditorEntityContextBus.h>

namespace InteractiveTutorials
{
    /// System component for InteractiveTutorials editor
    class InteractiveTutorialsEditorSystemComponent
        : public InteractiveTutorialsRequestBus::Handler
        , private AzToolsFramework::EditorEvents::Bus::Handler
        , public AZ::Component
    {
    public:
        AZ_COMPONENT(InteractiveTutorialsEditorSystemComponent, "{ff0e7abe-fe6c-449e-9e53-536388bdff1e}");
        static void Reflect(AZ::ReflectContext* context);

        InteractiveTutorialsEditorSystemComponent();
        ~InteractiveTutorialsEditorSystemComponent();

    private:
        static void GetProvidedServices(AZ::ComponentDescriptor::DependencyArrayType& provided);
        static void GetIncompatibleServices(AZ::ComponentDescriptor::DependencyArrayType& incompatible);
        static void GetRequiredServices(AZ::ComponentDescriptor::DependencyArrayType& required);
        static void GetDependentServices(AZ::ComponentDescriptor::DependencyArrayType& dependent);

        // AZ::Component
        void Activate();
        void Deactivate();
    };
} // namespace InteractiveTutorials
